from Grid1DCartesian import *
from Interpolator1DLinear import *
import numpy as np

# Create a grid with container's values are 2 times x values
# i.e. x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
#      y = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
# Since this function is linear, the interpolated value should equal
# the exact value.
def create_grid_basic():
	grid_step = np.array([1.0])
	grid_size = np.array([6])
	# Create an empty grid
	grid = Grid1DCartesian(grid_step, grid_size)
	grid.set_grid()
	# Create the container

	x = np.arange(0.5, (grid_size[-1] - 0.5), 1.0) * grid_step[-1]
	container = 2 * x
	grid.set_grid_container(container)

	return grid

def test_interpolator_basic():
	interpolator = Interpolator1DLinear()
	pos = np.arange(1, 5, 1)
	field = create_grid_basic()

	# interpolated field for all position
	field_i = interpolator(pos, field)

	for i in range(len(pos)):
		assert field_i[i] == 2 * pos[i]
