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
from pic.Field import *
from pic.fourierSolver import *



#initialize simulation
dt=0.09 #0.01* wpe0^-1
Tfinish=10 #10* wpe0^-1
xmin=0.0 #zero de0
xmax=10.0 #ten de0
T0=0.001 #temperature in dim units
n0=1 # in dim units
NPIC=5000 #number of one type of particles
Nsteps=int(Tfinish/dt)
Nx=np.array([100]) #number of grid cells
dx=np.array([(xmax-xmin)/Nx.item(0)]) #grid cell size, in de0
MMI=200000 #mass ratio
V0=0.0 #flow speed

#creating a plasma distribution
epc = ParticleCollection()
ipc = ParticleCollection()
epc, ipc = init_maxw(xmin=xmin, xmax=xmax, n0=n0, T0=T0, V0=V0, NPIC=NPIC, MMI=MMI, swidth=dx.item(0))

#creating a grid&field object
grid = Grid1DCartesian(dx,Nx,False)
grid.set_grid()
field = Field("Fourier", "linear", dt, grid)

pusher, velfixer = field.get_updaters("LeapFrog")

field.ex = np.zeros(grid.get_grid().size)
generator = SourceGenerator1DES()

i=0
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
	print('Timestep took ',str(int(1000*(time.time()-currtime))/1000),' seconds')
