""" @package Field
Field class
"""

from fourier_solver import fourier_solver

""" Calculate the field given a charge density.

Calculate the electrostatic field at a position on the grid
using an interpolation method.
"""
class Field:
    def __init__(self, FieldSolver_type, interpolation_type):
        self._FieldSolver = _initialize_solver(FieldSolver_type)
        self._interpolation_type = interpolation_type

    def _initialize_solver(FieldSolver_type):
        """Return the FieldSolver given its type.
        """
        if FieldSolver_type == "Fourier":
            return fourier_solver()
        else:
            raise ValueError("%s is not a field solver type"%FieldSolver_type)

    def solve(self, rho, grid, shift):
        """Solve the field using the field solver
        given a charge density (rho).
        """
        return self._FieldSolver(rho, grid, shift)
