"""@package Grid1DCartesian.py
Documentation for Grid1DCartesian class
"""

import numpy as np
from Grid1D import *

class Grid1DCartesian(Grid1D):
	"""
	Documentaiton for Grid1DCartesian class
	"""
	_type = "Cartesian"

	def set_grid(self):
                """
                Set the grid after it is initialized
                """
        	dx=self._grid_step.item(_Ndims-1)
		"""
		grid step size
		"""
		Nx=self._grid_size.item(_Ndims-1)
		"""
		number of grid nodes
		"""
		self._grid = np.linspace(0.0,dx*Nx,Nx)   
		self._grid_shifted = np.linspace(dx/2.0,dx*Nx-dx/2.0,Nx-1)                
	def set_grid_container(self,grid_container):
                """
                Setting values of grid container (i.e. fields or sources)
                """
		self._grid_container=grid_container

	def get_grid_container(self):
                """
                Accessing values of grid container (i.e. fields or sources)
                """
		return self._grid_container

