from unittest.mock import Mock
from unittest.mock import MagicMock
from Grid1DCartesian import *
from Interpolator1DLinear import *
import numpy as np

# Create a grid with container's values are 2 times x values
# i.e. x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
#      y = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
# Since this function is linear, the interpolated value should equal
# the exact value.
def test_interpolator_basic():
	interpolator = Interpolator1DLinear()

	# Create a mock grid that represent a field
	x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
	y = 2 * x
	field = Mock()
	field.get_grid_shifted = MagicMock(return_value = x)
	field.get_grid_container = MagicMock(return_value = y)
	
	pos = np.arange(1, 5, 1)
	# interpolated field for all position
	field_i = interpolator(pos, field)

	for i in range(len(pos)):
		assert field_i[i] == 2 * pos[i]
