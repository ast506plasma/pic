"""@package Shape1DTrangle.py
Documentation for Shape1DTrangle class
"""

import numpy as np
from Shape1D import *

class Shape1DTriangle(Shape1D):
	"""
	Documentaiton for Shape1DTriangle class
	"""
	_type = "Triangle"

	def __init__(self, size):
		"""
		The constructor
		"""
		self._size = size

	def get_height(self, position, particle_position):
		"""
		Return the value of the shape function at a given function.
		This function has to be overrided by the subclass.
		"""
		distance = np.abs(position - particle_position)
		return max(1  - distance / self._size, 0) / self._size
		
