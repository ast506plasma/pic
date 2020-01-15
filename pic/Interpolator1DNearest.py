"""@package Interpolator1DNearest
Documentation for Interpolator1DNearest class
"""

from pic.Interpolator1D import *
from scipy import interpolate
import numpy as np

class Interpolator1DNearest(Interpolator1D):
	"""
	Derived class of Interpolator1D using nearest interpolation
	"""

	def __call__(self, position):
		"""
		Return interpolated value of the field at the specified position
		"""
		# handles extrapolation cases
		# returns the value at the end of the grid
		if position <= self._grid_start:
			return self._field_start
		elif position >= self._grid_end:
			return self._field_end
		else:
			return self._interp(position)

	def _get_interp(self, field):
		grid = field.grid.get_grid()
		ex = field.get_field()
		self._grid_start = grid[0]
		self._grid_end = grid[-1]
		self._field_start = ex[0]
		self._field_end = ex[-1]

		return interpolate.interp1d(grid, ex, kind = "nearest")
