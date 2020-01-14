from pic.Field1D import Field1D
from pic.Grid1DCartesian import Grid1DCartesian
from pic.Shape1DTriangle import Shape1DTriangle
from pic.Particle import Particle
from pic.ParticleCollection import ParticleCollection
from pic.SourceGenerator1DES import SourceGenerator1DES
import numpy as np

PRECISION = 1e-5
GRID_SIZE = 100
STEP_SIZE = 2*np.pi / GRID_SIZE
TIME_STEP = 0.9

def get_1D():
    grid = Grid1DCartesian(np.array([STEP_SIZE]), np.array([GRID_SIZE]), False)
    grid.set_grid()
    field = Field1D("Fourier", "linear", TIME_STEP, grid)

    return grid, field

def test_field_Grid1DCartesian():
    grid, field = get_1D()

    assert field.Ndims == grid.get_Ndims()
    assert field._FieldSolver._type == "Fourier"

def test_field_solver_Grid1DCartesian(plot = False):
    # The main point is that the solver runs without issue.
    # To check the actual results, use plot = True and
    # confirm that the output is one sinusoidal wavelength
    # with values between +/- 0.5.
    grid, field = get_1D()

    x = grid.get_grid()
    rho = 0.1*np.sin(x)

    # Check that the grid was built correctly
    assert x[0] == 0.0
    assert np.abs(x[-1] - (STEP_SIZE * (GRID_SIZE - 1))) < PRECISION

    field.solve(rho)

    if plot:
        import matplotlib.pyplot as plt
        plt.plot(x, field.ex)

def test_field_updaters_1DLeapFrog():
    grid, field = get_1D()
    pusher, velfixer = field.get_updaters("LeapFrog")
    assert pusher.type == velfixer.type
    assert pusher.type == "1DLeapFrog"

    # Make two electrons and two ions
    shape = Shape1DTriangle(1)
    e1 = Particle(1, -1, "mobile", np.array([1.0]), np.array([0.0]), shape)
    e2 = Particle(1, -1, "mobile", np.array([2.0]), np.array([0.0]), shape)
    i1 = Particle(10, 1, "immobile", np.array([1.2]), np.array([0.0]), shape)
    i2 = Particle(10, 1, "immobile", np.array([1.8]), np.array([0.0]), shape)
    # Place them in collections
    ecoll = ParticleCollection()
    ecoll.set_particle_collection([e1, e2])
    icoll = ParticleCollection()
    icoll.set_particle_collection([i1, i2])

    # Make sure a zero field doesn't move anything
    field.ex = [0.0 for i in range(len(grid.get_grid()))]
    pusher(ecoll, field)
    pusher(icoll, field)
    assert e1.position == np.array([1.0])
    assert e2.position == np.array([2.0])
    assert i1.position == np.array([1.2])
    assert i2.position == np.array([1.8])

    # Calculate rho and field
    generator = SourceGenerator1DES()
    erho = generator.get_source(ecoll, grid.get_grid())
    irho = generator.get_source(icoll, grid.get_grid())
    rho = erho + irho
    field.solve(rho)

    # Accelerate particles
    velfixer(ecoll, field)
    velfixer(icoll, field)
    # Ions should not have moved
    assert i1.momentum == i2.momentum
    assert i1.momentum == np.array([0.0])
