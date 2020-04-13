from .database import ma
from .book import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True
