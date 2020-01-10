"""@package Interpolator
Documentation for Interpolator class (ABC)
"""

class Interpolator:
	"""
	Abstract base class for any interpolator
	"""
	def __init__(self):
		"""
		The constructor
		"""

	def __call__(self, position, field, grid):
		"""
		Return interpolated value of the field at the specified position
		"""
		pass
