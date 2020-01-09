"""@package Interpolator1DLinear
Documentation for Interpolator1DLinear class
"""

from Interpolator1D import *
from scipy import interpolate
import numpy as np

class Interpolator1DLinear(Interpolator1D):
	"""
	Derived class of Interpolator1D using linear interpolation
	"""

	def __call__(self, position, field):
		"""
		Return interpolated value of the field at the specified position
		"""
		p = interpolate.interp1d(field.get_grid_shifted(),\
							    field.get_grid_container(), kind = "linear")
		return p(position)
