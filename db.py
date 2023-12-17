import pymysql

conn = pymysql.connect(
    host='sql12.freesqldatabase.com	',
    database='sql12670741',
    user='sql12670741',
    password='',
    charset='',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

sql_query = """CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()


# import sqlite3

# conn = sqlite3.connect("books.sqlite")
# cursor = conn.cursor()
# sql_query = """CREATE TABLE book (
#     id integer PRIMARY KEY,
#     author text NOT NULL,
#     language text NOT NULL,
#     title text NOT NULL
# )"""
# cursor.execute(sql_query)
