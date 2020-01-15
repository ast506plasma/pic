"""@package Interpolator1D
Documentation for Interpolator1D class (ABC)
"""

from pic.Interpolator import *

class Interpolator1D(Interpolator):
	"""
	Interpolate a field in 1D to obtain a value at any given point
	"""

from pic.Interpolator1DLinear import *
from pic.Interpolator1DNearest import *
