#!/usr/bin/python3
""" My class module
"""


def class_to_json(obj):
	"""returns the dictionary description
	ARGS:
	-obj: object to be presented
	"""
	return obj.__dict__
