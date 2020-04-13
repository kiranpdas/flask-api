from models.book import Book
from models.author import Author


def get_all_authors():
    return Author.query.all()


def get_author(id):
    return Author.query.get(id)


def create_author(id, name):
    return Author(id=id, name=name)
