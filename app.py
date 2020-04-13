from flask import Flask, request, jsonify
from models.database import db, ma
from utils.model_ops import get_all_authors, get_author, create_author
from utils.orm_schemas import author_schema, authors_schema

# Initialize App
app = Flask(__name__)

# Configure DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db.init_app(app)
# Init ma
ma.init_app(app)


# New author
@app.route('/author', methods=['POST'])
def new_author():
    author = create_author(id=request.json['id'],
                           name=request.json['name'])
    db.session.add(author)
    db.session.commit()
    return author_schema.jsonify(author)

# Retrieve all authors
@app.route('/authors', methods=['GET'])
def get_authors():
    authors = authors_schema.dump(get_all_authors())
    return jsonify(authors)

# Update Author
@app.route('/author/<int:id>', methods=['PUT'])
def update_author(id):
    author = get_author(id)
    author.name = request.json['name']
    db.session.commit()
    return author_schema.jsonify(author)

# Delete author
@app.route('/author/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = get_author(id)
    db.session.delete(author)
    db.session.commit()
    return author_schema.jsonify(author)


if __name__ == '__main__':
    app.run(debug=True)
