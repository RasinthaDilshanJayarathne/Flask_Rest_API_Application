from flask import Flask, request, jsonify
import json
# import sqlite3
import pymysql

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect('books.sqlite')
    except pymysql.Error as e:
        print(e)
    return conn


@app.route('/books', methods=['GET', 'POST'])
def get_books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book")
        books = [
            # dict(id=row[0], author=row[1], language=row[2], title=row[3])
            dict(id=row['id'], author=row['author'],
                 language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]

        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        # sql = """INSERT INTO book (author, language, title) VALUES (?, ?, ?)"""
        sql = """INSERT INTO book (author, language, title) VALUES (%s, %s, %s)"""

        cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201


@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = dict(id=r[0], author=r[1], language=r[2], title=r[3])
            # book = dict(id=r['id'], author=r['author'],
            #             language=r['language'], title=r['title'])
        if book is not None:
            return jsonify(book), 200
        else:
            return "Book not found", 404

    if request.method == 'PUT':
        sql = """UPDATE book SET title = ?, author = ?, language = ? WHERE id = ?"""

        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }
        cursor.execute(sql, (title, author, language, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id = ?"""
        cursor.execute(sql, (id,))
        conn.commit()
        return 'Book deleted successfully', 200


if __name__ == '__main__':
    app.run(debug=True)
