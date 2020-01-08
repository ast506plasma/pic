"""@package Grid.py
Documentation for Grid class (ABC)
"""

import numpy as np

class Grid:
	"""
	Documentation for Grid class.
	"""
	def __init__(self, grid_step, grid_size):
		"""
		The constructor which delivers data of grid steps and number of nodes
		in the specific direction
		"""
		self._grid_step = grid_step
		self._grid_size = grid_size

	def set_grid(self, grid_step, grid_size):
		"""
		Set the grid after it is initialized
		"""
		pass

	def get_grid(self):
		"""
		Returns the grid
		"""
		return self._grid
	
	def get_grid_shifted(self):
		"""
		Returns the shifted grid
		"""
		return self._grid_shifted
	
	def set_grid_container(self, grid, is_shifted, grid_container):
		"""
		Setting values of grid container (i.e. fields or sources)
		"""
		pass

	def get_grid_container(self):
		"""
		Accessing values of grid container (i.e. fields or sources)
		"""
		pass
