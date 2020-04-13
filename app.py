from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize App
app = Flask(__name__)

# Configure DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Create Models
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref="books")


# Create Schemas
class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
book_schmea = BookSchema()
books_schema = BookSchema(many=True)

# New author
@app.route('/author', methods=['POST'])
def new_author():
    author = Author(id=request.json['id'], name=request.json['name'])
    db.session.add(author)
    db.session.commit()
    return author_schema.jsonify(author)

# Retrieve all authors
@app.route('/authors', methods=['GET'])
def get_authors():
    authors = authors_schema.dump(Author.query.all())
    return jsonify(authors)

# Update Author
@app.route('/author/<int:id>', methods=['PUT'])
def update_author(id):
    author = Author.query.get(id)
    author.name = request.json['name']
    db.session.commit()
    return author_schema.jsonify(author)

# Delete author
@app.route('/author/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get(id)
    db.session.delete(author)
    db.session.commit()
    return author_schema.jsonify(author)


if __name__ == '__main__':
    app.run(debug=True)
