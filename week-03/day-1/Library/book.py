class Book:
    
    def __init__(self, author, title, release_year):
        self._author = author
        self._title = title
        self._release_year = release_year
        # print(f'Creating a book {self._title}')

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def release_year(self):
        return self._release_year

    def __str__(self):
        return f'{self.author}: {self.title} ({self.release_year})'

