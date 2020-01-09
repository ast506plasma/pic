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

	def __call__(self, position, field):
		"""
		Return interpolated value of the field at the specified position
		"""
		grid = field.get_grid_shifted()
		grid_field = field.get_grid_container()
		
		# handles extrapolation cases
		# returns the value at the end of the grid
		if position <= grid[0]:
			return grid_field[0]
		elif position >= grid[-1]:
			return grid_field[-1]

		p = interpolate.interp1d(grid, grid_field, kind = "nearest")
		return p(position)