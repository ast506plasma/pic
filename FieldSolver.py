""" @package Field Solver
Field Solver ABC
"""

""" Abstract class for solving the field.
"""
class FieldSolver:
    def __init__(self):
        self._type = "None"

    def __call__(self, rho, grid, shift):
        pass
