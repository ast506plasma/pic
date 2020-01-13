"""@package Interpolator1DNearest
Documentation for Interpolator1DNearest class
"""

from Interpolator1D import *
from scipy import interpolate
import numpy as np

class Interpolator1DNearest(Interpolator1D):
	"""
	Derived class of Interpolator1D using nearest interpolation
	"""

	def __call__(self, position, field, grid):
		"""
		Return interpolated value of the field at the specified position
		"""
		# handles extrapolation cases
		# returns the value at the end of the grid
		if position <= grid[0]:
			return field[0]
		elif position >= grid[-1]:
			return field[-1]

		p = interpolate.interp1d(grid, field, kind = "nearest")
		return p(position)
