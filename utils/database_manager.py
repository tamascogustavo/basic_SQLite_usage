# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-11 08:48:02
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-11 12:12:07
"""

This code will use SQLite as DATABASES

"""

from .database_connection import DatabaseConnection



book_database = "data.db"

def create_table():
	with DatabaseConnection(book_database) as connection:
		
		cursor = connection.cursor()
		#perform a query
		cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
		

def insert_book(name,author):
	with DatabaseConnection(book_database) as connection:

		cursor = connection.cursor()

		cursor.execute('INSERT INTO books VALUES(?,?,0)', (name,author))


def get_all_books():
	with DatabaseConnection(book_database) as connection:
		cursor = connection.cursor()

		cursor.execute('SELECT * FROM books')
		#Save the data to variable
		books = cursor.fetchall()#Will give a list of tuples
		#Convert to a list of dict 
		books = [{"name":item[0], "author":item[1], "read":item[2]} for item in books]
	
	return books


def mark_book_as_read(name):
	
	with DatabaseConnection(book_database) as connection:

		cursor = connection.cursor()

		cursor.execute('UPDATE books SET read=1 WHERE name = ?', (name,))

	

def delete_book(name):
	
	with DatabaseConnection(book_database) as connection:
		
		cursor = connection.cursor()

		cursor.execute('DELETE FROM books WHERE name = ?', (name,))

	