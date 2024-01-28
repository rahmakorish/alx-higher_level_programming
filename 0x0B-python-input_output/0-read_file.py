#!/usr/bin/python3
"""input"""


def read_file(filename=""):
	with open(filename, encoding="UTF8") as f:
		file_data = f.read()
		print(file_data)
