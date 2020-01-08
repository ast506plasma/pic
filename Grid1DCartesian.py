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
		Method sets the grid after it is initialized
		dx is the grid step size; Nx is the number of grid nodes
		We assume that the domain is from Lbeg=0 to Lend=dx*(Nx-1),
		usual grid - same boundaries with Nx nodes,
		shifted grid - from dx/2 to Lend - dx/2 with Nx-1 nodes
		"""
		dx=self._grid_step.item(self._Ndims-1)
		Nx=self._grid_size.item(self._Ndims-1)
		self._grid = np.linspace(0.0,dx*(Nx-1),Nx)
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

