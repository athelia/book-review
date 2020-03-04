from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc, desc, update
import os

db = SQLAlchemy()

class User(db.Model):
    """User of book-review app."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)


class Book(db.Model):
    """Book object."""

    __tablename__ = 'books'

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author = db.Column(db.String(), nullable=True)
    title = db.Column(db.String(), nullable=False)
    isbn_13 = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(), nullable=True)


class Review(db.Model):
    """A user's review of a book."""

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    review_date = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    text = db.Column(db.String(), nullable=True)

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.book_id'),
                        nullable=False)


def connect_to_db(app):
    """Connect db to Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///books'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print('Connected to DB.')