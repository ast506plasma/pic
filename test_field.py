from Field import Field
from Grid1DCartesian import Grid1DCartesian
import numpy as np
import pdb

PRECISION = 1e-5
GRID_SIZE = 100
STEP_SIZE = 2*np.pi / GRID_SIZE

def test_field_Grid1DCartesian():
    grid = Grid1DCartesian(np.array([STEP_SIZE]), np.array([GRID_SIZE]), False)
    field = Field("Fourier", "linear", grid)

    assert field.Ndims == grid.get_Ndims()
    assert field._FieldSolver._type == "Fourier"

def test_field_solver_Grid1DCartesian(plot = False):
    # The main point is that the solver runs without issue.
    # To check the actual results, use plot = True and
    # confirm that the output is one sinusoidal wavelength
    # with values between +/- 0.5.
    grid = Grid1DCartesian(np.array([STEP_SIZE]), np.array([GRID_SIZE]), False)

    grid.set_grid()
    x = grid.get_grid()
    pdb.set_trace()
    rho = 0.1*np.sin(x)

    field = Field("Fourier", "linear", grid)

    assert x[0] == 0.0
    assert np.abs(x[-1] - (STEP_SIZE * (GRID_SIZE - 1))) < PRECISION

    field.solve(rho)

    if plot:
        import matplotlib.pyplot as plt
        plt.plot(x, field.ex)
