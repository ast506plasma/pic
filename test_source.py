from SourceGenerator1DES import *
from Grid1DCartesian import *
from Shape1DTriangle import *
from Particle import *
from ParticleCollection import *
import numpy as np

# Maximum error when comparing float numbers
PRECISION = 1e-5


def test_source_generator():
	dx = np.array([1.0])
	Nx = np.array([10])
	gg = Grid1DCartesian(dx,Nx,False)
	gg.set_grid()
	grid = gg.get_grid()
	gridhalf = gg.get_grid_shifted()

	s = Shape1DTriangle(1)
	pc = ParticleCollection()
	p1 = Particle(1,-1, np.array([1.2,0.2,-0.2]), np.array([1,1,1]), s)
	p2 = Particle(4, 1, np.array([0.4,0.2,0.2]), np.array([1,1,1]), s)
	pc.add_particles(p1)
	pc.add_particles(p2)

	SourceGenerator1DES.get_source(pc,grid)
