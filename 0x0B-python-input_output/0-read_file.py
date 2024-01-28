#!/usr/bin/python3
"""input"""


def read_file(filename=""):
	"""read file"""	
	with open(filename, encoding="UTF8") as f:
		file_data = f.read()
		if not file_data:
			pass 
		else:
			print(file_data)
