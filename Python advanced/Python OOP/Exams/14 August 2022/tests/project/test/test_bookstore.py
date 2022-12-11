from project.bookstore import Bookstore
import unittest


class BookstoreTests(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(3)

    def test_init(self):
        self.assertEqual(3, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ex.exception))

    def test_books_limit(self):
        self.bookstore.books_limit = 2
        self.assertEqual(2, self.bookstore.books_limit)

    def test_len(self):
        self.bookstore.receive_book('a', 1)
        self.bookstore.availability_in_store_by_book_titles['b'] = 2
        self.assertEqual(3, len(self.bookstore))

    def test_receive_book_exception(self):
        self.bookstore.receive_book('a', 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('a', 6)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_book(self):
        res = self.bookstore.receive_book('a', 2)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles['a'])
        self.assertEqual('2 copies of a are available in the bookstore.', res)
        self.assertEqual(2, len(self.bookstore))
        self.assertEqual({'a': 2}, self.bookstore.availability_in_store_by_book_titles)

        res2 = self.bookstore.receive_book('a', 1)
        self.assertEqual('3 copies of a are available in the bookstore.', res2)
        self.assertEqual(3, len(self.bookstore))
        self.assertEqual({'a': 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_add_existing_book(self):
        self.bookstore.receive_book('a', 1)
        res = self.bookstore.receive_book('a', 1)
        self.assertEqual('2 copies of a are available in the bookstore.', res)
        self.assertEqual({'a': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, len(self.bookstore))

    def test_sell_book_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('a', 1)
        self.assertEqual('Book a doesn\'t exist!', str(ex.exception))

    def test_sell_book_not_enough_copies(self):
        self.bookstore.receive_book('a', 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('a', 2)
        self.assertEqual('a has not enough copies to sell. Left: 1', str(ex.exception))

    def test_sell_book(self):
        self.bookstore.receive_book('a', 2)
        self.bookstore.receive_book('b', 1)

        res = self.bookstore.sell_book('a', 1)
        self.assertEqual('Sold 1 copies of a', res)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual(2, len(self.bookstore))
        self.assertEqual({'a': 1, 'b': 1}, self.bookstore.availability_in_store_by_book_titles)

        res2 = self.bookstore.sell_book('a', 1)
        self.assertEqual('Sold 1 copies of a', res2)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(1, len(self.bookstore))
        self.assertEqual({'a': 0, 'b': 1}, self.bookstore.availability_in_store_by_book_titles)

        res3 = self.bookstore.sell_book('b', 1)
        self.assertEqual('Sold 1 copies of b', res3)
        self.assertEqual(3, self.bookstore.total_sold_books)
        self.assertEqual(0, len(self.bookstore))
        self.assertEqual({'a': 0, 'b': 0}, self.bookstore.availability_in_store_by_book_titles)

    def test_str(self):
        self.bookstore.receive_book('a', 2)
        self.bookstore.receive_book('b', 1)
        self.bookstore.sell_book('a', 2)
        self.bookstore.sell_book('b', 1)
        self.assertEqual('Total sold books: 3\nCurrent availability: 0\n - a: 0 copies\n - b: 0 copies', str(self.bookstore))


if __name__ == '__main__':
    unittest.main()