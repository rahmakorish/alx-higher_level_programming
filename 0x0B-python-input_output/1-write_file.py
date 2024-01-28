#!/usr/bin/python3
"""module to write into file"""


def write_file(filename="", text=""):
	"""write to file 
	Args:
	- filename:given file
	- text:text to be written inside file
	"""
	with open(filename, 'w') as f:
		return f.write(text)
