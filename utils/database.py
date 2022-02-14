# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-11 08:48:02
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-11 11:01:57
"""

This code will use SQLite as DATABASES

"""

import sqlite3



book_database = "data.db"

def create_table():
	#make connection
	connection = sqlite3.connect(book_database)
	#create a cursor
	cursor = connection.cursor()

	#perform a query
	cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
	
	#commit
	connection.commit()
	#close connection
	connection.close()

def insert_book(name,author):
	connection = sqlite3.connect(book_database)

	cursor = connection.cursor()

	cursor.execute('INSERT INTO books VALUES(?,?,0)', (name,author))

	connection.commit()

	connection.close()

def get_all_books():
	connection = sqlite3.connect(book_database)
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM books')
	#Save the data to variable
	books = cursor.fetchall()#Will give a list of tuples
	#Convert to a list of dict 
	books = [{"name":item[0], "author":item[1], "read":item[2]} for item in books]
	#because we are only reading the data we dont need to commit
	connection.close()

	return books


def mark_book_as_read(name):
	connection = sqlite3.connect(book_database)

	cursor = connection.cursor()

	cursor.execute('UPDATE books SET read=1 WHERE name = ?', (name,))

	connection.commit()

	connection.close()

def delete_book(name):
	connection = sqlite3.connect(book_database)

	cursor = connection.cursor()

	cursor.execute('DELETE FROM books WHERE name = ?', (name,))

	connection.commit()

	connection.close()
