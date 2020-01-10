"""@package Grid.py
Documentation for Grid class (ABC)
"""

import numpy as np

class Grid:
	"""
	Documentation for Grid class.
	"""
	def __init__(self, grid_step, grid_size, is_shifted):
		"""
		The constructor which delivers data of grid steps and number of nodes
		in the specific direction
		"""
		self._grid_step = grid_step
		self._grid_size = grid_size
		self._is_shifted = is_shifted

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

	def get_if_shifted(self):	
		"""
		Returns the is_shifted, telling whether the grid is shifted or not
		"""
		return self._is_shifted

	def set_grid_container(self, grid_container):
		"""
		Setting values of grid container (i.e. fields or sources)
		"""
		self._grid_container=grid_container

	def get_grid_container(self):
		"""
		Accessing values of grid container (i.e. fields or sources)
		"""
		return self._grid_container

	def get_Ndims(self):
		"""
		returning number of dimensions for the field solver purposes
		"""
		return self._Ndims
