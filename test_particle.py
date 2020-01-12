from Particle import *
from Shape1DTriangle import *
import numpy as np

PRECISION = 1e-5

# check if two float numbers are close enoguh
# Do not compare 2 float numbers directly
def are_floats_equal(float1, float2):
	diff = np.abs(float1 - float2)
	return diff < PRECISION

def test_particle_basic():
	mass = 2.5
	charge = -4.4
	position = np.array([1.0, 2.0, 3.0])
	momentum = np.array([-1.3, 2.2, -3.1])
	shape = Shape1DTriangle(2)

	p = Particle(mass, charge, "mobile", position, momentum, shape)
	assert are_floats_equal(p.get_mass(), 1.0)
	assert are_floats_equal(p.get_charge(), charge)
	assert p.position.all() == position.all()
	assert p.momentum.all() == momentum.all()
	assert p.get_shape() == shape
