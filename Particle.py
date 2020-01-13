"""@package Particle.py
Documentation for Particle class
"""

import numpy as np
from Shape import *

class Particle:
	"""
	Documentation for Particle class
	"""
	def __init__(self, mass, charge, type, position, momentum, shape):
		"""
		The constructor
		"""
		self._mass = mass
		self._charge = charge

		# Check valid particle type
		if type in ['mobile', 'immobile']:
			self.type = type
		else:
			raise ValueError("%s is not a valid particle type."%type)

		self.position = position
		self.momentum = momentum
		self._shape = shape

		# Check if mobile. If so, its mass must be 1
		if ((self.type == "mobile") and (self._mass != 1)):
			self._mass = 1
			print("Mass of mobile particle set to 1.")
		# Check if mobile. If so, its charge must be -1
		if ((self.type == "mobile") and (self._charge != -1)):
			self._charge = -1
			print("Charge of mobile particle set to -1.")

	def get_mass(self):
		"""
		Returns mass
		"""
		return self._mass

	def get_charge(self):
		"""
		Returns charge
		"""
		return self._charge

	def get_shape(self):
		"""
		Returns shape
		"""
		return self._shape

	def get_closest(self, grid):
		"""
		Find the index of the closest grid node to the particle
		"""
		minarray=np.abs(grid-self.position*np.ones(grid.size))
		xmin=np.amin(minarray)
		xind = np.where(minarray == xmin)
		return xind[0][0]
