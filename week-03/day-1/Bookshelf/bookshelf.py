class Bookshelf:
    def __init__(self, name='', books=[]):
        self._name = name
        self._books = books
        print(f'Creating a bookshelf {self._name}')

    def add_book(self, a_book):
        self._books.append(a_book)
        print(f'Bookshelf {self._name} is adding book {a_book.title}')

    def find_lightest(self):
        lightest = []
        lightest_weight = self._books[0].weight
        for book in self._books:
            if book.weight < lightest_weight:
                lightest_weight = book.weight
                lightest = list([book.title])
            elif book.weight == lightest_weight:
                lightest.append(book.title)
        return lightest

    def find_largest_page(self):
        most = []
        most_pages = self._books[0]._page_numer
        for book in self._books:
            if book._page_numer < most_pages:
                most_pages = book._page_numer
                most = list([book.title])
            elif book._page_numer == most_pages:
                most.append(book.title)
        return most
