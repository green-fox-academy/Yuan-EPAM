class Library:
    def __init__(self, name, book_shelf= []):
        self._name = name
        self._book_shelf = book_shelf
        print(f'Creating a library: {self._name}')

    def add_book_shelf(self, a_book_shelf):
        self._book_shelf.append(a_book_shelf)
        print(f'Library {self._name} added a bookshelf:')
        print(a_book_shelf)


