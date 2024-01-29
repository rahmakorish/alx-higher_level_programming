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
	
	def to_json(self, attrs=None):
		"""retrieves a dictionary representation"""
		if attrs is not None:
			for x in attrs:
				if x == 'first_name':
					return self.__dict__.get('first_name')
				if x == 'age':
					return self.age
				if x == 'lastt_name':
                                	return self.last_name
		return (self).__dict__
