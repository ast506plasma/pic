""" @package Field
Field class
"""

from pic.Field import Field
from pic.fourierSolver import fourierSolver
import pic.Interpolator1D as Interpolator1D
import pic.Pusher as Pusher
import pic.VelocityFixer as VelocityFixer
import numpy as np

""" Calculate the field given a charge density.

Calculate the electrostatic field at a position on the grid
using an interpolation method.
"""
class Field1D(Field):
    def __init__(self, FieldSolver_type, interp_type, time_step, grid):
        self.grid = grid
        self.Ndims = self.grid.get_Ndims()
        self.time_step = time_step
        self._ex = np.zeros(grid.get_grid().size)
        self._FieldSolver = self._initialize_solver(FieldSolver_type)
        self._interp_type = interp_type
        self._interpolator = self._initialize_interp()

    def _initialize_solver(self, FieldSolver_type):
        """Return the FieldSolver given its type.
        """
        if FieldSolver_type == "Fourier":
            return fourierSolver()
        else:
            raise ValueError("%s is not a field solver type"%FieldSolver_type)

    def _initialize_interp(self):
        """Return the Interpolator given its type.
        """
        try:
            interp = getattr(Interpolator1D, "Interpolator1D{}".format(self._interp_type))
        except AttributeError:
            raise ValueError("Unknown interpolator 1D%s"%self._interp_type)

        return interp(self)

    def solve(self, rho):
        """Solve the field using the field solver
        given a charge density (rho).
        Update the interpolator.
        """
        self._ex = self._FieldSolver(rho, self.grid)
        self._interpolator = self._initialize_interp()

        return

    def interpolate(self, position):
        """Interpolate field values at given positions.
        """

        return self._interpolator(position)

    def get_updaters(self, type):
        """Obtain the updaters (pusher, velocity fixer) for this field.
        """
        type = "1D{}".format(type)

        try:
            pusher = getattr(Pusher, "Pusher{}".format(type))
        except AttributeError:
            raise ValueError("Unknown pusher type %s"%type)

        try:
            velfix = getattr(VelocityFixer, "VelocityFixer{}".format(type))
        except AttributeError:
            raise ValueError("Unknown velocity fixer type %s"%type)

        return pusher(), velfix()
