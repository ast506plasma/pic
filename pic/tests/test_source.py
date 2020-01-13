from pic.SourceGenerator1DES import *
from pic.Grid1DCartesian import *
from pic.Shape1DTriangle import *
from pic.Particle import *
from pic.ParticleCollection import *
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
	p1 = Particle(1,-1, "mobile", np.array([2.0]), np.array([0.0]), s)
	p2 = Particle(4, 1, "immobile", np.array([1.0]), np.array([0.0]), s)
	pc.add_particles(p1)
	pc.add_particles(p2)

	generator = SourceGenerator1DES()
	source = generator.get_source(pc,grid)
	assert source.size == 10
	assert source.item(0) == 0.0
	assert source.item(1) == 1.0
	assert source.item(2) == -1.0


	p1 = Particle(1,-1, "mobile", np.array([2.2]), np.array([0.0]), s)
	p2 = Particle(4, 1, "immobile", np.array([8.9]), np.array([0.0]), s)
	pc2 = ParticleCollection()
	pc2.add_particles(p1)
	pc2.add_particles(p2)

	source = generator.get_source(pc2,grid)
	assert source.size == 10
	assert source.item(1) == 0.0
	assert np.abs(source.item(2)+0.8) < PRECISION
	assert np.abs(source.item(9)-0.9) < PRECISION


def test_source_generator_adv():
	dx = np.array([1.0])
	Nx = np.array([10])
	gg = Grid1DCartesian(dx,Nx,False)
	gg.set_grid()
	grid = gg.get_grid()
	gridhalf = gg.get_grid_shifted()

	s = Shape1DTriangle(1)
	pc3 = ParticleCollection()
	p1 = Particle(1,-1, "mobile", np.array([2.2]), np.array([0.0]), s)
	p2 = Particle(4, 1, "immobile", np.array([1.7]), np.array([0.0]), s)
	pc3.add_particles(p1)
	pc3.add_particles(p2)

	generator = SourceGenerator1DES()
	source = generator.get_source(pc3,grid)
	assert source.size == 10
	assert np.abs(source.item(2) + 0.1) < PRECISION
