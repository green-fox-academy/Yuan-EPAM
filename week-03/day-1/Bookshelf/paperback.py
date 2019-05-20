from book import Book

class Paperback(Book):
    def __init__(self, title, author, release_year, page_number):
        Book.__init__(self, title, author, release_year, page_number)
        self._weight = page_number * 10 + 20 

    @property 
    def weight(self):
        return self._weight
