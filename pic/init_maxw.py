"""@package init_maxw.py
Documentation for maxwell distribution initialization
"""

from pic.ParticleCollection import *
from pic.Shape1DTriangle import *
import numpy as np
import random

def init_maxw(xmin=1.0, xmax=9.0, n0=1, T0=0.01, V0=0.0, NPIC=1000, MMI=100, swidth=0.1):
	"""
	c=e=em=mu=1, de0=1, we0=1
	function to initialize uniform plasma slab of particles with density n0,
	temperature T0, flow velocity V0, number of mobile particles NPIC,
	mass ratio MMI
	"""
	i=0
	xe=[]
	pex=[]
	pey=[]
	pez=[]
	xi=[]
	pix=[]
	piy=[]
	piz=[]
	while (i<NPIC):
		xe.append(xmin+(xmax-xmin)*random.random())
		while True:
			x=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				pex.append(2*np.sqrt(2*T0)*x+V0)
				break
		while True:
			x=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				pey.append(2*np.sqrt(2*T0)*x)
				break
		while True:
			x=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				pez.append(2*np.sqrt(2*T0)*x)
				break
		while True:
			xion=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				pix.append(0.0)
				break
		while True:
			x=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				piy.append(2*np.sqrt(2*T0/MMI)*x)
				break
		while True:
			x=5*(random.random()-0.5)
			y=random.random()
			if(np.exp(-x*x)>=y):
				piz.append(2*np.sqrt(2*T0/MMI)*x)
				break
		i+=1
	xi=[x for x in xe]

	s = Shape1DTriangle(swidth)
	epc = ParticleCollection()
	ipc = ParticleCollection()
	i=0
	while (i<NPIC):
		p1 = Particle(1,-1, "mobile", np.array([xe[i]]), np.array([pex[i]]), s)
		p2 = Particle(MMI, 1, "immobile", np.array([xi[i]]), np.array([0.0]), s)
		epc.add_particles(p1)
		ipc.add_particles(p2)
		i+=1
	return epc, ipc
