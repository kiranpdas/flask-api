from .database import ma
from .author import Author


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
