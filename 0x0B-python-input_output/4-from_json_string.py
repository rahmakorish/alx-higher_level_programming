#!/usr/bin/python3
"""this Module  returns an object (Python data structure) 
represented by a JSON string"""
import json


def from_json_string(my_str):
	"""function for deserialization
	ARGS:
	-my_str:string to be converted
	"""
	return json.loads(my_str)
