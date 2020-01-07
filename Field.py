""" @package Field
Field class
"""

from fourier_solver import fourier_solver

""" Calculate the field given a charge density.

Calculate the electrostatic field at a position on the grid
using an interpolation method.
"""
class Field:
    def __init__(self, FieldSolver_type, interpolation_type, grid):
        self._FieldSolver = self._initialize_solver(FieldSolver_type)
        self._interpolator = self._initialize_interp(interpolation_type)
        self.ex = None
        self.grid = grid

    def _initialize_solver(self, FieldSolver_type):
        """Return the FieldSolver given its type.
        """
        if FieldSolver_type == "Fourier":
            return fourierSolver()
        else:
            raise ValueError("%s is not a field solver type"%FieldSolver_type)

    def _initialize_interp(self, interpolation_type):
        """Return the Interpolator given its type.
        """
        return "Under construction"
        # if interpolation_type == "Fourier":
        #     return fourierSolver()
        # else:
        #     raise ValueError("%s is not an interpolator type"%interpolator_type)

    def solve(self, rho, shift):
        """Solve the field using the field solver
        given a charge density (rho).
        """
        self.ex = self._FieldSolver(rho, self.grid, shift)

        return

    def interpolate(self, position):
        if self.ex is None:
            raise RuntimeError("The field hasn't been solved yet.")
        else:
            pass
            # return self._interpolator(position, self.ex, self.grid)
