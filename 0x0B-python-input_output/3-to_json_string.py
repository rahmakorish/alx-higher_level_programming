#!/usr/bin/python3
"""this Module returns the 
JSON representation of an object
"""
import json


def to_json_string(my_obj):
	"""return JSON reperesentation
	ARGS:
	my_obj:object represented
	"""
	return json.dumps(my_obj)
