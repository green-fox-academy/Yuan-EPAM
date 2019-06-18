import sys
sys.path.append('.')
sys.path.append('..')

import os
import json
import requests

import db_psql

class NestoriaAPI:
    def __init__(self, endpoint, param):
        self._endpoint = endpoint
        self._param = param
        self._res = None
        self._data = None

    @property
    def param(self):
        return self._param
    
    @param.setter
    def param(self, **args):
        self._param.update(**args)

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, new_endpoint):
        self._endpoint = new_endpoint

    def check_api_connection(self, status_code):
        """
        Check API if works
        """
        if status_code == 200:
            print("200 API of Nestoria requested successfully!")
        elif status_code == 400:
            print("400 Bad request")
        elif status_code == 403:
            print("403 API of Nestoria call was forbidden. Reached maximum calls")
        else:
            print(f"Misterous error : {status_code}")

    def request_api_get(self, param= None):
        """
        Uses Get method to request API server
        """
        if param:
            self._param.update(param)
        self._res = requests.get(self._endpoint, self._param)
        self.check_api_connection(self._res.status_code)
        return self._res

    def load_json(self):
        """ 
        Currently, only support load JSON data
        """
        if self._res.status_code == 200:
            self._data = json.loads(self._res.content)
            print('Loaded API JSON data.')

    def extract_data_source(self):
        return self._data['request']

    def extract_listing(self):
        """
        Extract listing data, which is houses detailed infomation
        """
        return self._data['response']

    def get_current_page_num(self):
        return self._data['response']['page']

    def retrieve_one_page_data(self, page_num= 1):
        """
        @page_num : The number of page data to retrieve
        """
        self.request_api_get({"page" : page_num})
        self.load_json()
        page_res = self.get_current_page_num()
        if page_res < page_num:
            print('Warming: Page number input out of range!')
        else:
            print(self._data['request'])

    def retrieve_all_pages_data(self, page_num= 1):
        res = None
        while True:
            print(f'Extracting page {page_num}')
            self.request_api_get({"page" : page_num})
            self.load_json()
            page_res = self.get_current_page_num()
            if page_res < page_num:
                print('Extracted Done!')
                return res
            else:
                if res:
                    res.append(self._data)
                else:
                    res = self._data

    def save_page_data(self, to_folder= 'json', to_file= 'api_nestoria.json', page_num= 1, all= False):
        to_file_path = os.path.join('.', 'data', to_folder, to_file)
        if all:
            self.save_all_page_data(to_folder, to_file)
        else: 
            if self._data:
                page_res = self.get_current_page_num()
                if page_res != page_num:
                    # if input page number is new, reload data before writing json data to file
                    self.request_api_get({"page" : page_num})
                    self.load_json()
                with open(to_file_path, 'w') as f:
                    json.dump(self._data, f)
                print(f'Saved page {page_num} data to {to_file_path}')

    def save_all_page_data(self, to_folder, to_file):
        page_num = 1
        while True:
            to_file_path = os.path.join('.', 'data', to_folder, str(page_num) + to_file, )
            self.request_api_get({"page" : page_num})
            self.load_json()
            page_res = self.get_current_page_num()
            if page_res < page_num:
                print('Done')
                break
            with open(to_file_path, 'w') as f:
                json.dump(self._data, f)
            print(f'Saved page {page_num} data to {to_file_path}')
            page_num += 1


nestoria_endpoint = 'https://api.nestoria.co.uk/api'
nestoria_param = {
    "encoding" : 'json',
    "action" : "search_listings",
    "country" : "uk",
    "listing_type" : "buy",
    "place_name" : "somerset",
    "number_of_results" :15,
    "page" : 5
}
nestoria_api = NestoriaAPI(nestoria_endpoint, nestoria_param)
# print(nestoria_api.param)
# res = nestoria_api.request_api_get({"page" : 10})
# nestoria_api.load_json()
# print(nestoria_api.extract_data_source())
# nestoria_api.request_api_get()
# nestoria_api.retrieve_one_page_data(2)
nestoria_api.save_page_data(all= True)