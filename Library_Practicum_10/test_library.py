import unittest

from library import add_book, count_books, remove_book, search_book


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.books = {}

    def test_add_book(self):
        add_book(self.books, 1, "Dune")
        self.assertEqual(self.books, {1: "Dune"})

    def test_add_duplicate_book_raises_error(self):
        add_book(self.books, 1, "Dune")
        with self.assertRaises(ValueError):
            add_book(self.books, 1, "Another book")

    def test_search_book(self):
        add_book(self.books, 1, "Dune")
        self.assertEqual(search_book(self.books, 1), "Dune")
        self.assertIsNone(search_book(self.books, 2))

    def test_remove_book(self):
        add_book(self.books, 1, "Dune")
        self.assertEqual(remove_book(self.books, 1), "Dune")
        self.assertEqual(self.books, {})

    def test_remove_missing_book_raises_error(self):
        with self.assertRaises(ValueError):
            remove_book(self.books, 1)

    def test_count_books(self):
        add_book(self.books, 1, "Dune")
        add_book(self.books, 2, "Foundation")
        self.assertEqual(count_books(self.books), 2)


if __name__ == "__main__":
    unittest.main()
