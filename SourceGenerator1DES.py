"""@package SourceGenerator1DES.py
Documentation for SourceGenerator1DES class
"""

import numpy as np
from SourceGenerator1D import *
from Shape1DTriangle import *

class SourceGenerator1DES(SourceGenerator1D):
	"""
	Documentation for source generator class with Ndims=1D
	and electrostatic field equation (i.e. we need to deposit charge density only)
	according to the structure of the Grid object
	"""
	_type = "ES"

	def get_closest(grid,xpart):
		"""
		finding an index of the closest grid note to the particle
		"""
		minarray=np.abs(grid-xpart*np.ones(grid.size))
		xmin=np.amin(minarray)
		xind = np.where(minarray == xmin)
		return xind[0][0]

	def get_source(ParticleCollection,grid):
		"""
		creating an empty source of the same size as grid
		and iterating over all particles
		"""
		source_size = grid.size #size of the source array
		dx = np.abs(grid.item(1)-grid.item(0)) #grid cell size
		source = np.zeros(source_size) # creating an empty source array
		w1 = 1.0 #there should be some weight coefficient; before, it was  grid.size/ParticleCollection.particles.size, but now it seems weird
		s = Shape1DTriangle(dx)
		for part in ParticleCollection.particles:
			id_closest=SourceGenerator1DES.get_closest(grid,part.position)
			charge=part.get_charge()
			w2 = s.get_height(grid.item(id_closest),part.position)
			source[id_closest]+=charge*w1*w2
		return source
