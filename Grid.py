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
		The constructor
		"""
		self._grid_step = grid_step
		self._grid_size = grid_size
		
	def set_grid(self, grid_step, grid_size):
		"""
		Set the grid after it is initialized
		""" 
		pass
	
	def set_grid_container(self, grid, is_shifted, grid_container):
		"""
		Setting values of grid container (i.e. fields or sources)
		"""
		pass
	
	def get_grid_container(self, grid, is_shifted, grid_container):
		"""
		Accessing values of grid container (i.e. fields or sources)
		"""
		pass
