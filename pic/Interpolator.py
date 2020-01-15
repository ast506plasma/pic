"""@package Interpolator
Documentation for Interpolator class (ABC)
"""

class Interpolator:
	"""
	Abstract base class for any interpolator
	"""
	def __init__(self, field):
		"""
		The constructor
		"""
		self._interp = self._get_interp(field)

	def __call__(self, position):
		"""
		Return interpolated value of the field at the specified position
		"""
		pass

	def _get_interp(self, field):
		"""
		Return the interpolator given the field.
		"""
		pass
