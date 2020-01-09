""" @package Fourier Solver
Fourier Solver class
"""

from FieldSolver import FieldSolver
import numpy as np

""" Fourier method for solving the field given rho and grid.
"""
class fourierSolver(FieldSolver):
    def __init__(self):
        self._type = "Fourier"

    def __call__(self, rho, grid, shift):
        """Return the field along an axis given
        the charge density, grid, and shift.
        """
        nx = len(rho)
        dx = grid.cell_size # Figure out how this implemented by Grid class
        lx = dx * float(nx)

        Frho = np.fft.fft(rho)

        Fex = Frho
        for i in range(1, nx):
            k = 2*np.pi*float(i) / lx
            k_i = lx / (2*np.pi*float(i))
            Fex[i] = -Frho[i] * 1j*k_i * np.exp(1j*k*dx*shift)

        Ex = [np.real(xx) for xx in np.fft.ifft(Fex)]

        return Ex
