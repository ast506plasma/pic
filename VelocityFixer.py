"""@package Velocity Fixer
"""

class VelocityFixer:
    def __init__(self):
        """
        Initialize the velocity fixer.
        """
        self.type = None

    def __call__(self, collection, field):
        pass

class VelocityFixer1D(VelocityFixer):
    """Accelerate the mobile particles in a collection.
    """
    def __init__(self):
        self.type = "1D"

    def __call__(self, collection, field):
        firsttype = collection[0].type
        if firsttype == "immobile":
            # If particles are immobile, nothing occurs
            return

        grid = field.grid.get_grid()
        gridhalf = field.grid.get_grid_shifted()
        grid_step = grid[1] - grid[0]

        force_func = lambda gridpos, pos: 1.0-np.abs(gridpos - pos) / grid_step

        for pp in collection:
            # Make sure all particles are of the same type
            assert(pp.type == firsttype,
                   "Particles in collection are not of the same type")

            force = 0.0
            posidx = pp.get_closest(gridhalf)
            force = field.ex[posidx] * force_func(gridhalf[posidx], pp.position)

            if pp.type == 'mobile':
                # Accelerate particle
                pp.momentum -= 0.5*field.time_step*force
            else:
                pass

        return
