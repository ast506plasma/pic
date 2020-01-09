"""@package Interpolator
Documentation for Interpolator class (ABC)
"""

class Interpolator:
	def __init__(self, type1):
		"""
		The constructor
		"""
		set_interpolator(self, type1)

	def set_interpolator(self, type1)
		"""
		Set the type of interpolator after initialization
		"""
		self._type = type1

	def __call__(self, position, field):
		"""
		Return interpolated value of the field at the specified position
		"""
		pass
