from unittest.mock import Mock
from unittest.mock import MagicMock
from Interpolator1DNearest import *
import numpy as np

PRECISION = 1e-7

# Create a grid with container's values are 2 times x values
# i.e. x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
#      y = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
# Since this function is linear, the interpolated value should equal
# the exact value.
def test_interpolator_basic():
	interpolator = Interpolator1DNearest()

	# Create a mock grid that represent a field
	x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
	y = 2 * x
	field = Mock()
	grid = x #MagicMock(return_value = x)
	field = y #MagicMock(return_value = y)

	# test basic cases
	assert np.abs(interpolator(1.5, field, grid) - 3.0) < PRECISION
	assert np.abs(interpolator(1.9, field, grid) - 3.0) < PRECISION
	assert np.abs(interpolator(2.2, field, grid) - 5.0) < PRECISION

	# test a boundary case
	# for boundary case the interpolator returns the value at the lower
	# grid point
	assert np.abs(interpolator(2.0, field, grid) - 3.0) < PRECISION

	# test for position is outside shifted-grid but stil inside grid
	assert np.abs(interpolator(0.1, field, grid) - 1.0) < PRECISION
	assert np.abs(interpolator(4.8, field, grid) - 9.0) < PRECISION
