from pic.ParticleCollection import *
from pic.Shape1DTriangle import *
import numpy as np

# compare 2 Particles
def compare_particles(particle1, particle2):
	assert particle1.get_mass() == particle2.get_mass()
	assert particle1.get_charge() == particle2.get_charge()
	assert particle1.position.all() == particle2.position.all()
	assert particle1.momentum.all() == particle2.momentum.all()
	assert particle1.type == particle2.type
	assert particle1.get_shape() == particle2.get_shape()

def test_particle_collection_add_particles():
	s = Shape1DTriangle(1)
	pc = ParticleCollection()
	p1 = Particle(1,-1, "mobile", np.array([1.2,0.2,-0.2]), np.array([1,1,1]), s)
	p2 = Particle(4, 1, "immobile", np.array([0.4,0.2,0.2]), np.array([1,1,1]), s)
	pc.add_particles(p1)
	pc.add_particles(p2)

	compare_particles(pc.particles[0], p1)
	compare_particles(pc.particles[1], p2)

def test_particle_collection_set_particles():
	s = Shape1DTriangle(1)
	p1 = Particle(1, -1, "mobile", np.array([1.2,0.2,-0.2]), np.array([1,1,1]), s)
	particle_array = np.array([p1, p1, p1, p1])

	pc = ParticleCollection()
	assert pc.particles.shape[-1] == 0

	# test whether set_particles works properly with empty collections
	pc.set_particle_collection(particle_array)
	assert pc.particles.shape[-1] == 4
	for i in range(4):
		compare_particles(pc.particles[i], p1)

	# test whether set_particles works properly with non-empty collections
	p2 = Particle(4, 1, "immobile", np.array([0.4,0.2,0.2]), np.array([1,2,3]), s)
	pc.set_particle_collection(np.array([p2]))
	assert pc.particles.shape[-1] == 1
	compare_particles(pc.particles[0], p2)
