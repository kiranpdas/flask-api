from models.book_schema import BookSchema
from models.author_schema import AuthorSchema

# Create Schemas
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
book_schmea = BookSchema()
books_schema = BookSchema(many=True)