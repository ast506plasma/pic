"""@package Shape.py
Documentation for Shape class (ABC)
"""

import numpy as np

class Shape:
	"""
	Documentation for Shape class.
	"""
	def __init__(self, size):
		"""
		The constructor
		"""
		self._size = size

	def set_shape(self, size):
		"""
		Set the shape after it is initialized
		""" 
		self._size = size

	def get_height(self, position, particle_position):
		"""
		Return the value of the shape function at a given function.
		This function has to be overrided by the subclass.
		"""
		pass
