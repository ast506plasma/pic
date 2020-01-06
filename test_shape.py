from Shape1DTriangle import *
import numpy as np

# Maximum error when comparing float numbers
PRECISION = 1e-5

def test_shape_basic():
	s = Shape1DTriangle(1)
	assert s._Ndims == 1
	assert s._type == 'Triangle'
	assert s._size == 1

def test_shape_set_shape():
	s = Shape1DTriangle(4)
	s.set_shape(2)
	assert s._size == 2
	

def test_shape_get_height():
	s = Shape1DTriangle(2)
	
	particle_position = 1
	
	assert np.abs(s.get_height(1, particle_position) - 0.5) < PRECISION
	assert np.abs(s.get_height(0, particle_position) - 0.25) < PRECISION
	assert np.abs(s.get_height(2, particle_position) - 0.25) < PRECISION
	assert np.abs(s.get_height(3, particle_position)) < PRECISION
	assert np.abs(s.get_height(-4, particle_position)) < PRECISION
