from Field import Field
import numpy as np

def field_solver_test(plot = False):
    # Fake Grid class for simple initialization
    class Grid:
        def __init__(self, x):
            self.cell_size = x[1] - x[0]

    x = np.linspace(0,2*np.pi,100)
    rho = 0.1*np.sin(x)

    grid = Grid(x)
    field = Field("Fourier", 3, grid)

    field.solve(rho, 0.0)
    
    if plot:
        import matplotlib.pyplot as plt
        plt.plot(x, rho)
        plt.plot(x, field.ex)
