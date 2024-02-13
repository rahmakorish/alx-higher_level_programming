#!/usr/bin/python3
""" My class module
"""


class Student():
	"""class to define student"""

	def __init__(self, first_name, last_name, age):
		"""intialization"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	
	def to_json(self):
		"""retrieves a dictionary representation"""
		return (self).__dict__
