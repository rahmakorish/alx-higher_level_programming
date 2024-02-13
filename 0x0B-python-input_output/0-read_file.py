#!/usr/bin/python3
"""Module 0-reaf"_file
read from given file
"""


def read_file(filename=""):
	"""read file and print to std
	Args:
	- filename:given file
	"""	
	with open(filename, 'r') as f:
		file_data = f.read()
		print(file_data.strip())
