"""@package Particle.py
Documentation for Particle class
"""

import numpy as np
from Shape1DTriangle import *

class Particle:
	"""
	Documentation for Particle class
	"""
	def __init__(self, mass, charge, position, momentum, shape):
		"""
		The constructor
		"""
		self._mass = mass
		self._charge = charge
		self.position = position
		self.momentum = momentum
		self._shape = shape

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

	
