"""@package Interpolator1DLinear
Documentation for Interpolator1DLinear class
"""

from Interpolator1D import *
import numpy as np

class Interpolator1DLinear(Interpolator1D):
	"""
	Derived class of Interpolator1D using linear interpolation
	"""

	def __call__(self, position, field):
		"""
		Return interpolated value of the field at the specified position
		"""
		grid = field.get_grid_shifted()
		dx = grid[1] - grid[0]
		grid_field = field.get_grid_container()
		
		# handles extrapolation cases
		# returns the value at the end of the grid
		if position <= grid[0]:
			return grid_field[0]
		elif position >= grid[-1]:
			return grid_field[-1]

		# finds the nearest grid points first
		distance = np.abs(position - grid)

		min_distance = np.amin(distance)
		min_index = np.where(distance == min_distance)

		# returns the average if the position is perfectly at the  middle
		# between 2 points
		if min_index[0].shape[-1] == 2:
			return np.mean(grid_field[min_index[0]])

		# else proceeds to find nearest field and the second nearest field
		nearest_field = grid_field[min_index][0]
		distance[min_index] = 1e10

		second_min_distance = np.amin(distance)
		second_min_index = np.where(distance == second_min_distance)
		second_nearest_field = grid_field[second_min_index][0]

		return (dx - min_distance) * nearest_field + \
			   (dx - second_min_distance) * second_nearest_field
