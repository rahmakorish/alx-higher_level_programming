#!/usr/bin/python3
"""this Module writes an Object to a text file, 
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
	"""save json to file
	ARGS:
	- my_obj:object to be written
	- filename:file to write to
	"""
	data = json.dumps(my_obj)
	with open(filename, 'w') as f:
		f.write(data)		
