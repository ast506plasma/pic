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
	assert np.abs(gridhalf.item(1)-1.5)<PRECISION
	assert grid.size == 10
	assert gridhalf.size == 9


def test_grid_container():
	dx = np.array([1.0])
	Nx = np.array([10])
	gg = Grid1DCartesian(dx,Nx)
	gg.set_grid()
	grid = gg.get_grid()
	gridhalf = gg.get_grid_shifted()
	sinwave=np.sin(grid)
	sinwaveshifted=np.sin(gridhalf)
	gg.set_grid_container(sinwave)
	cont=gg.get_grid_container()

	assert np.abs(cont.item(0)-0.0)<PRECISION
	assert np.abs(cont.item(1)-np.sin(1.0))<PRECISION
	assert np.abs(cont.item(9)-np.sin(9.0))<PRECISION
	assert cont.size == 10

	gg.set_grid_container(sinwaveshifted)
	contshifted=gg.get_grid_container()

	assert np.abs(contshifted.item(0)-np.sin(0.5))<PRECISION
	assert np.abs(contshifted.item(1)-np.sin(1.5))<PRECISION
	assert np.abs(contshifted.item(8)-np.sin(8.5))<PRECISION
	assert contshifted.size == 9
