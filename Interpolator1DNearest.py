"""@package Interpolator1DNearest
Documentation for Interpolator1DNearest class
"""

from Interpolator1D import *
# from scipy import interpolate
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

		# finds the nearest grid point
		distance = np.abs(position - grid)
		min_distance = np.amin(distance)
		min_index = np.where(distance == min_distance)

		return grid_field[min_index[0][0]]
		
		# If scipy is installed on travis machine, comment above and uncomment
		# below.
		#p = interpolate.interp1d(field.get_grid_shifted(),\
		#					    field.get_grid_container(), kind = "nearest")
		#return p(position)
