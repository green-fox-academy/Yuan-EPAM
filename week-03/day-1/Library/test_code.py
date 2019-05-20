from library import Library
from bookshelf import Bookshelf
from book import Book

print('-'*10 + 'Create Library' + '-'*10)
lib_a = Library('greenfox')
print('-'*10 + 'Create Bookshel' + '-'*10)
shelf_1 = Bookshelf('1')
shelf_2 = Bookshelf('2')
print('-'*10 + 'Create Book' + '-'*10)
book_a = Book(author= 'Bob', title= 'Bob of cook1',  release_year= '2019/01/01')
book_b = Book(author= 'Bob', title= 'Bob of cook2',  release_year= '2019/01/02')
book_c = Book(author= 'Bob', title= 'Bob of cook3',  release_year= '2019/01/03')
book_d = Book(author= 'Alic', title= 'Beauty1 of Alice',  release_year= '2019/01/01')
book_e = Book(author= 'Alic', title= 'Beauty2 of Alice',  release_year= '2019/01/05')
book_f = Book(author= 'Tom', title= 'Tom of game1',  release_year= '2019/01/01')
book_g = Book(author= 'Tom', title= 'Tom of game2', release_year= '2019/01/02')
book_h = Book(author= 'Tom', title= 'Tom of game3', release_year= '2019/01/06')
book_i = Book(author= 'Bob', title= 'bob of cook4',  release_year= '2019/01/010')
book_j = Book(author= 'Nick', title= 'Nick of Python1',  release_year= '2019/02/01')
book_k = Book(author= 'Nick', title= 'Nick of Python2',  release_year= '2019/02/02')
book_l = Book(author= 'Tom', title= 'Tom of game4',  release_year= '2019/02/05')
print('-' * 50)
books = [book_a, book_b, book_c, book_d, book_e, book_f, book_g, book_h, book_i, book_j, book_k, book_l]
for book in books:
    shelf_1.add_book(book)
    print(book)

print()
# print(shelf_1)
lib_a.add_book_shelf(shelf_1)

