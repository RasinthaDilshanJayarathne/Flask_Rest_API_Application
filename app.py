from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "Chinua Achebe",
        "language": "English",
        "title": "Things Fall Apart",
    },
    {
        "id": 1,
        "author": "Chinua Achebe",
        "language": "English",
        "title": "Arrow of God",
    },
    {
        "id": 2,
        "author": "Gabriel Garcia Marquez",
        "language": "Spanish",
        "title": "One Hundred Years of Solitude",
    },
    {
        "id": 3,
        "author": "Harper Lee",
        "language": "English",
        "title": "To Kill a Mockingbird",
    },
    {
        "id": 4,
        "author": "Jane Austen",
        "language": "English",
        "title": "Pride and Prejudice",
    },
    {
        "id": 5,
        "author": "J.K. Rowling",
        "language": "English",
        "title": "Harry Potter and the Sorcerer's Stone"
    }
]


@app.route('/books', methods=['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return 'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id'] + 1

        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
        return 'Book not found', 404

    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }
                return jsonify(updated_book)

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)

        return 'Book not found', 404


if __name__ == '__main__':
    app.run(debug=True)
