"""@package Interpolator1D
Documentation for Interpolator1D class (ABC)
"""

from Interpolator import *

class Interpolator1D(Interpolator):
	"""
	Interpolate a field in 1D to obtain a value at any given point
	"""

	def __call__(self, position, field, grid):
		"""
		Return interpolated value of the field at the specified position
		"""
		pass
