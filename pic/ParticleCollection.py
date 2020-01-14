"""@package ParticleCollection
Documentaion for Particle Collection
"""

from pic.Particle import *

class ParticleCollection:
	"""
	Stores particles
	"""
	def __init__(self):
		"""
		Creates an empty particle collection
		"""
		self.particles = np.empty([0], dtype = Particle)

	def set_particle_collection(self, particles):
		"""
		Removes all existing particles in the collection and replaces with
		new ones
		"""
		self.particles = particles

	def add_particles(self, particles):
		"""
		Add new particle(s) into the collection
		"""
		self.particles = np.append(self.particles, particles)
