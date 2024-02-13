#!/usr/bin/python3
"""module to write into file"""


def append_write(filename="", text=""):
	"""write to file 
	Args:
	- filename:given file
	- text:text to be written inside file
	"""
	with open(filename, 'a') as f:
		return f.write(text)
