"""@package Pusher
"""

import numpy as np

class Pusher:
    def __init__(self):
        """
        Initialize the pusher.
        """
        self.type = None

    def __call__(self, collection, field):
        pass

class Pusher1DLeapFrog(Pusher):
    def __init__(self):
        self.type = "1DLeapFrog"

    def __call__(self, collection, field):
        """Push particles in a collection.
        """
        firsttype = collection.particles[0].type
        grid = field.grid.get_grid()
        gridhalf = field.grid.get_grid_shifted()
        grid_step = grid[1] - grid[0]

        force_func = lambda gridpos, pos: 1.0-np.abs(gridpos - pos) / grid_step

        for pp in collection.particles:
            # Make sure all particles are of the same type
            assert(pp.type == firsttype,
                   "Particles in collection are not of the same type")

            force = 0.0
            posidx = pp.get_closest(gridhalf)
            force = field.ex[posidx] * force_func(gridhalf[posidx], pp.position)

            if pp.type == 'mobile':
                # Push particle
                pp.momentum -= 0.5*field.time_step*force
                pp.position += field.time_step*pp.momentum
            else:
                pass

            # Recalculate coordinate if particle is away from the grid after the push
            if pp.position < grid[0]:
                pp.position += grid[-1] - grid[0]
            if pp.position > grid[-1]:
                pp.position += grid[0] - grid[-1]

        return
