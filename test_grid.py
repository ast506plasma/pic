from Grid1DCartesian import *
import numpy as np

# Maximum error when comparing float numbers
PRECISION = 1e-5


def test_grid_basic():
	dx = np.array([1.0])
	Nx = np.array([10])
	gg = Grid1DCartesian(dx,Nx)
	gg.set_grid()
	grid = gg.get_grid()
	gridhalf = gg.get_grid_shifted()

	assert gg._Ndims == 1
	assert gg._type == 'Cartesian'
	assert np.abs(grid.item(2)-2.0)<PRECISION
	assert np.abs(gridhalf.item(0)-0.5)<PRECISION
	assert grid.size == 10
	assert gridhalf.size == 9
