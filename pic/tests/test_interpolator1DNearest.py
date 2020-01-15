from unittest.mock import Mock
from unittest.mock import MagicMock
from pic.Interpolator1DNearest import *
import numpy as np

PRECISION = 1e-7

# Create a grid with container's values are 2 times x values
# i.e. x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
#      y = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
# Since this function is linear, the interpolated value should equal
# the exact value.
def test_interpolator_basic():
	# Create a mock grid that represent a field
	x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
	y = 2 * x

	field = Mock()
	field.grid = MagicMock()
	field.grid.get_if_shifted = MagicMock(return_value = False)
	field.grid.get_grid = MagicMock(return_value = x)
	field.get_field = MagicMock(return_value = y)

	interpolator = Interpolator1DLinear(field)

	# test basic cases
	assert np.abs(interpolator(1.5) - 3.0) < PRECISION
	assert np.abs(interpolator(1.9) - 3.8) < PRECISION
	assert np.abs(interpolator(2.2) - 4.4) < PRECISION

	# test a boundary case
	# for boundary case the interpolator returns the value at the lower
	# grid point
	assert np.abs(interpolator(5.0) - 9.0) < PRECISION

	# test for position is outside shifted-grid but stil inside grid
	assert np.abs(interpolator(0.1) - 1.0) < PRECISION
	assert np.abs(interpolator(4.8) - 9.0) < PRECISION
