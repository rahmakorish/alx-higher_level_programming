#!/usr/bin/python3
"""this Module creats an Object to a texit file, 
using a JSON representation"""
import json


def load_from_json_file(filename):	
	"""save from json file
	ARGS:
	- filename:file to save from
	"""
	with open(filename, 'r') as f:
		file_data = f.read(json.loads(data))
		print (file_data.strip())
