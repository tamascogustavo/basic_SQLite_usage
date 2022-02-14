# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-11 08:47:36
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-11 11:57:41

from utils import database_manager	


def menu():
	USER_CHOICE = input("""

	Enter:

	'a' to add a new book
	'l' to list all books
	'r' to mark a book as read
	'd' to delete a book
	'q' to quit

	Your choice: """)
	return USER_CHOICE



def prompt_add():
	name = input("Enter the book name: ")
	author = input("Enter author: ")
	database_manager.insert_book(name, author)

def prompt_list():
	for book in database_manager.get_all_books():
		read = "Yes" if book["read"]==1 else "No"
		print(f"The book {book['name']} by {book['author']}, is read {read}")

def prompt_read():
	name = input("Enter the name of ther book you finished reading: ")
	database_manager.mark_book_as_read(name)


def prompt_delete():
	name = input("Enter the name of the book you want to delete: ")

	database_manager.delete_book(name)

def main():
	execute = {
			"a": prompt_add,
			"l": prompt_list,
			"r": prompt_read,
			"d": prompt_delete
		}
	

	database_manager.create_table()
	user_input = menu()

	while user_input != "q":
		task = execute[user_input]
		task()
		user_input = menu()

if __name__=='__main__':
	main()
















