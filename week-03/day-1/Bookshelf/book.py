class Book:
    def __init__(self, title, author, release_year, page_number=0):
        self._title = title
        self._author = author
        self._release_year = release_year
        self._page_numer = page_number
        self._weight = None
        # print(f'Creating a book {self._title}')

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def release_year(self):
        return self._release_year

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self):
        pass

    def __str__(self):
        return f'Book info: \n\
                    - author: {self._author} \n\
                    - title: {self._title} \n\
                    - year: {self._release_year}'