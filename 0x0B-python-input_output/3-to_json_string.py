#!/usr/bin/python3
import json
"""this Module returns the 
JSON representation of an object
"""
def to_json_string(my_obj):
	"""return JSON reperesentation
	ARGS:
	my_obj:object represented
	"""
	return json.dumps(my_obj)
