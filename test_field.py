from Field import Field
import numpy as np
import matplotlib.pyplot as plt

def field_solver_test():
    # Fake Grid class for simple initialization
    class Grid:
        def __init__(self, x):
            self.cell_size = x[1] - x[0]

    x = np.linspace(0,2*np.pi,100)
    rho = 0.1*np.sin(x)

    grid = Grid(x)
    field = Field("Fourier", 3, grid)

    field.solve(rho, 0.0)
    # plt.plot(x, rho)
    plt.plot(x, field.ex)
