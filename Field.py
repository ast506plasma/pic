""" @package Field
Field class
"""

from fourierSolver import fourierSolver
from Interpolator1DLinear import Interpolator1DLinear
from Interpolator1DNearest import Interpolator1DNearest

""" Calculate the field given a charge density.

Calculate the electrostatic field at a position on the grid
using an interpolation method.
"""
class Field:
    def __init__(self, FieldSolver_type, interp_type, grid):
        self.grid = grid
        self.Ndims = self.grid.get_Ndims()
        self._FieldSolver = self._initialize_solver(FieldSolver_type)
        self._interpolator = self._initialize_interp(interp_type)
        self.ex = None

    def _initialize_solver(self, FieldSolver_type):
        """Return the FieldSolver given its type.
        """
        if FieldSolver_type == "Fourier":
            return fourierSolver()
        else:
            raise ValueError("%s is not a field solver type"%FieldSolver_type)

    def _initialize_interp(self, interp_type):
        """Return the Interpolator given its type.
        """
        if self.Ndims == 1:
            switcher1D = {
                "linear": Interpolator1DLinear(),
                "nearest": Interpolator1DNearest(),
            }
            interp = switcher1D.get(interp_type, 1) # 1 for error catcher
        else:
            raise ValueError(Ndims) # Invalid dimension

        # Check if interp_type was available for Ndims
        if isinstance(interp, int):
            raise ValueError("%s is not a valid %dD interpolator"%(interp_type,
                                                                   self.Ndims))
        else:
            return interp

    def solve(self, rho):
        """Solve the field using the field solver
        given a charge density (rho).
        """
        self.ex = self._FieldSolver(rho, self.grid)

        return

    def interpolate(self, position):
        if self.ex is None:
            raise RuntimeError("The field hasn't been solved yet.")
        else:
            if self.grid.is_shifted == True:
                grid = self.grid.get_grid_shifted()
            else:
                grid = self.grid.get_grid()

        return self._interpolator(position, self.ex, grid)
