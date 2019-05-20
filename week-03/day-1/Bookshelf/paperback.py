from book import Book

class Paperback(Book):
    @property 
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self):
        self._weight = self._page_numer * 10 + 20