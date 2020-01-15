""" @package Field Solver
Field Solver ABC
"""

""" Abstract class for solving the field.
"""
class FieldSolver:
    def __init__(self):
        """
        The constructor
        """
        self._type = "None"

    def __call__(self, rho, grid):
        """
        Return a field solved on a grid given
        the charge density (rho)
        """
        pass
