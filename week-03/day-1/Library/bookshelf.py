class Bookshelf:
    def __init__(self, name= 'shelf_one', books= []):
        self._name = name
        self._books = books
        # print(f'Creating a bookshelf: {self._name}')

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        self._books.remove(book)

    def check_bookshelf(self):
        if len(self._books) <= 0:
            print(f'There is no book in {self._name}')
            raise IndexError(f'There is no book in {self._name}')

    def get_favourite_author(self):
        self.check_bookshelf()
        author_count = {}
        favourite_author = []
        max_book = 0
        for book in self._books:
            if book.author in author_count.keys():
                author_count[book.author] += 1
            else:
                author_count[book.author] = 1
        # The number of the author of most books in a shelf, could be 1, or many
        for author, book_count in author_count.items():
            print(f'author: {author}, book_count: {book_count}')
            if book_count > max_book:
                max_book = book_count
                favourite_author = list([author])
            elif book_count == max_book:
                favourite_author.append(author)
        return ' '.join(favourite_author)

    def get_earliest_published(self):
        self.check_bookshelf()
        earliest_published = []
        earliest_date = self._books[0].release_year
        for book in self._books:
            if book.release_year < earliest_date:
                earliest_date = book.release_year
                earliest_published = list([book.title])
            elif book.release_year == earliest_date:
                earliest_published.append(book.title)
        return ', '.join(earliest_published)

    def get_lastest_published(self):
        self.check_bookshelf()
        lastest_published = []
        lastest_date = self._books[0].release_year
        for book in self._books:
            if book.release_year > lastest_date:
                lastest_date = book.release_year
                lastest_published = list([book.title])
            elif book.release_year == lastest_date:
                lastest_published.append(book.title)
        return ', '.join(lastest_published)

    def __str__(self):
        favourite_author = self.get_favourite_author()
        earliest_published = self.get_earliest_published()
        lastest_published = self.get_lastest_published()
        return f'In bookshelf {self._name}: \n \
            - favourite author: {favourite_author} \n \
            - earliest published book: {earliest_published} \n \
            - lastest published book: {lastest_published}'


        
            

    

        