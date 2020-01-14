from pic.ParticleCollection import *
from pic.Shape1DTriangle import *
from pic.init_maxw import *
import numpy as np
from scipy.stats import norm


TEMP_PRECISION = 1e-1 #precision to calculate temperature

def test_init_maxw():
	pc = ParticleCollection()
	pc = init_maxw(xmin=1.0, xmax=9.0, n0=1, T0=0.01, V0=0.0, NPIC=100, MMI=100, swidth=0.1)
	assert pc.particles.size == 200

	assert pc.particles[0].get_mass() == 1
	assert pc.particles[0].get_charge() == -1
	assert pc.particles[0].position >= 1.0
	assert pc.particles[0].position <= 9.0
	assert pc.particles[0].type == "mobile"

	assert pc.particles[1].get_mass() == 100
	assert pc.particles[1].get_charge() == 1
	assert pc.particles[1].position >= 1.0
	assert pc.particles[1].position <= 9.0
	assert pc.particles[1].momentum == 0.0
	assert pc.particles[1].type == "immobile"


def test_temperature():
	pc = ParticleCollection()
	pc = init_maxw(xmin=1.0, xmax=9.0, n0=1, T0=0.01, V0=0.0, NPIC=1000, MMI=100, swidth=0.1)
	pex =[]
	for part in pc.particles:
		if (part.type == "mobile"):
			pex.append(part.momentum)
	mu, std = norm.fit(pex)
	ElectronTemp = std*std/4.0
	assert np.abs((ElectronTemp - 0.01)/ElectronTemp)<TEMP_PRECISION
