from sqlalchemy import func

from model import connect_to_db, db, Book
from server import app

def seed_books():
    """Seed books into database."""

    print('Seeding books...')

    # Empty database
    Book.query.delete()
    
    counter = 0
    with open('books.txt') as file:
        for line in file:
            line = line.rstrip()
            author, title, isbn, genre = line.split('|')
            book = Book(author=author, title=title, isbn_13=int(isbn), genre=genre)

            db.session.add(book)
            counter += 1

        db.session.commit()
        print(f'{counter} books seeded.')


def set_val_book_id():
    """Set value for the next book_id after seeding database"""

    result = db.session.query(func.max(Book.book_id)).one()
    max_id = int(result[0])

    query = "SELECT setval('books_book_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app)
    seed_books()
    set_val_book_id()
