from book import Book

class HardcoverBook(Book):
    @property
    def weight(self):
        return self._weight