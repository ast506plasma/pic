""" @package Field
Field class
"""

"""
Object to hold all the field components.
"""
class Field:
    def __init__(self, FieldSolver_type, interp_type, time_step, grid):
        """
        The constructor
        """
        self.grid = grid
        self.Ndims = self.grid.get_Ndims()
        self.time_step = time_step
        self._ex = np.zeros(grid.get_grid().size)
        self._FieldSolver = self._initialize_solver(FieldSolver_type)
        self._interpolator = self._initialize_interp(interp_type)

    def _initialize_solver(self, FieldSolver_type):
        """
        Return a FieldSolver
        """
        return

    def _initialize_interp(self, interp_type):
        """
        Return an interpolator
        """
        return

    def get_field(self):
        """
        Return the field
        """
        return self._ex

    def solve(self, rho):
        """
        Solve the field given rho, the charge density
        """
        return

    def interpolate(self, position):
        """
        Interpolate the field at the position
        """
        return

    def get_updaters(self, type):
        """
        Return the particle updaters appropriate to this field
        """
        return
