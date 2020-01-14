import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import sys
from scipy.stats import norm
import time


from pic.init_maxw import *
from pic.ParticleCollection import *
from pic.Shape1DTriangle import *
from pic.Grid1DCartesian import *
from pic.SourceGenerator1DES import *
from pic.Pusher import *
from pic.VelocityFixer import *
from pic.Interpolator1DLinear import *
from pic.Field1D import *
from pic.fourierSolver import *
from pic.output import *

#importing simulation parameters into main.py
from conf import *

#initialize simulation
Nsteps=int(Tfinish/dt) #calculating number of timesteps
Nx=np.array([Grid_Size]) #creating an array with grid size
dx=np.array([(xmax-xmin)/Nx.item(0)]) #grid cell size, in de0

#creating a plasma distribution
epc = ParticleCollection()
ipc = ParticleCollection()
epc, ipc = init_maxw(xmin=xmin, xmax=xmax, n0=n0, T0=T0, V0=V0, NPIC=NPIC, MMI=MMI, swidth=dx.item(0))

#creating a grid&field object
grid = Grid1DCartesian(dx,Nx,False)
grid.set_grid()
field = Field1D("Fourier", "linear", dt, grid)

pusher, velfixer = field.get_updaters("LeapFrog")

generator = SourceGenerator1DES()

i=0
full_output(field,epc,ipc,datadir,i)
while(i<Nsteps):
	currtime=time.time()
	print("Nstep=",str(i+1), ", time=",str(int((i+1)*dt*1000)/1000), "wpe0^-1")
	pusher(epc, field)
	pusher(ipc, field)
	erho = generator.get_source(epc, grid.get_grid())
	irho = generator.get_source(ipc, grid.get_grid())
	rho = erho + irho
	field.solve(rho)
	velfixer(epc, field)
	velfixer(ipc, field)
	i+=1
	if(i%Nout ==0):
		full_output(field,epc,ipc,datadir,i)
	print('Timestep took ',str(int(1000*(time.time()-currtime))/1000),' seconds')
