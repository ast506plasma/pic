"""@package Velocity Fixer
"""

import numpy as np

class VelocityFixer:
    def __init__(self):
        """
        Initialize the velocity fixer.
        """
        self.type = None

    def __call__(self, collection, field):
        pass

class VelocityFixer1DLeapFrog(VelocityFixer):
    """Accelerate the mobile particles in a collection.
    """
    def __init__(self):
        self.type = "1DLeapFrog"

    def __call__(self, collection, field):
        firsttype = collection.particles[0].type
        if firsttype == "immobile":
            # If particles are immobile, nothing occurs
            return

        grid = field.grid.get_grid()
        gridhalf = field.grid.get_grid_shifted()
        grid_step = grid[1] - grid[0]

        for pp in collection.particles:
            # Make sure all particles are of the same type
            assert pp.type == firsttype,\
                   "Particles in collection are not of the same type"

            def force_func(gridpos, pos):
                return 1.0-np.abs(gridpos - pos) / grid_step

            force = 0.0
            posidx = pp.get_closest(gridhalf)
            force = field.ex[posidx] * force_func(gridhalf[posidx], pp.position)

            # Accelerate particle
            pp.momentum -= 0.5*field.time_step*force

        return
