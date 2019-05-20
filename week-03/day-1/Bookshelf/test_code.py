from bookshelf import Bookshelf
from hardcover import HardcoverBook
from paperback import Paperback

shelf_a = Bookshelf('1')
hardcover_1 = HardcoverBook(title='hard 1', author= 'Bob', release_year= '2019/01/01', page_number= 10)
hardcover_2 = HardcoverBook(title= 'hard 2', author= 'Bob', release_year= '2019/01/02', page_number= 20)
paperback_1 = Paperback(title= 'paperback 1', author= 'Tom', release_year= '2019/01/01', page_number= 30)
paperback_2 = Paperback(title= 'paperback 2', author= 'Tom', release_year= '2019/01/02', page_number= 10)
hardcover_3 = HardcoverBook(title= 'hard 3', author= 'Alice', release_year= '2019/01/01', page_number= 20)
paperback_3 = Paperback(title= 'paperback 3', author= 'Alice', release_year= '2019/01/02', page_number= 100)

books = [hardcover_1, hardcover_2, paperback_1, paperback_2, hardcover_3, paperback_3]

for book in books:
    shelf_a.add_book(book)

shelf_a.find_lightest()
shelf_a.find_largest_page()