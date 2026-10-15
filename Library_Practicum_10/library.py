def add_book(books, book_id, title):
    if book_id in books:
        raise ValueError('Duplicate book ID')
    books[book_id] = title
    return books

def search_book(books, book_id):
    return books.get(book_id)

def remove_book(books, book_id):
    if book_id not in books:
        raise ValueError('Book not found')
    return books.pop(book_id)

def count_books(books):
    return len(books)
"""Library functions for Practicum 10."""
