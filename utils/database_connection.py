# -*- coding: utf-8 -*-
# @Author: gustavotamascohotmail.com
# @Date:   2022-02-11 11:22:20
# @Last Modified by:   gustavotamascohotmail.com
# @Last Modified time: 2022-02-11 12:05:07

import sqlite3



class DatabaseConnection:
	def __init__(self, host):
		self.connection = None
		self.host = host

	def __enter__(self):
		self.connection = sqlite3.connect(self.host)
		return self.connection

	def __exit__(self, exc_type, exc_value, exc_tb):
		#sometimes we don't need to commit however its not a problem to leave it here
		if exc_type or exc_value or exc_tb:
			self.connection.close()
		else:
			self.connection.commit()
			self.connection.close()

		