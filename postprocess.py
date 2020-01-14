#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import sys
from scipy.stats import norm
import time


def output(datadir,xe, pex, grid, ex, dt, i,xmax):
    #histograms of all particles in x-pex space
    plt.clf()
    plt.hist2d(xe, pex, bins=(40, 40), cmap=plt.cm.jet)
    plt.colorbar()
    plt.clim(0,40)    
    plt.xlim([0,10])
    plt.xlabel(r'$x/d_{e0}$')
    plt.ylabel(r'$p_{ex}/m_ec$')
    omegape=r'$\,\omega_{pe0}^{-1}$'
    plttitle="t="+str(int(dt*i*10000.0)/10000.0)+omegape
    plt.title(plttitle)
    plt.savefig(datadir+'x_px_'+str(i)+'.png')
    
    #trajectories of all particles in x-pex space
    plt.clf()
    plt.plot(xe, pex,'.')
    plt.xlim([0,10])
    plt.xlabel(r'$x/d_{e0}$')
    plt.ylabel(r'$p_{ex}/m_ec$')
    omegape=r'$\,\omega_{pe0}^{-1}$'
    plttitle="t="+str(int(dt*i*10000.0)/10000.0)+omegape
    plt.title(plttitle)
    plt.savefig(datadir+'traj_x_px_'+str(i)+'.png')


    #electric field Ex
    plt.clf()
    plt.plot(grid, ex)
    plt.xlim([0,10])
    plt.xlabel(r'$x/d_{e0}$')
    plt.ylabel(r'$E_{x}$')
    omegape=r'$\,\omega_{pe0}^{-1}$'
    plttitle="t="+str(int(dt*i*10000.0)/10000.0)+omegape
    plt.title(plttitle)
    plt.savefig(datadir+'ex_'+str(i)+'.png')

    #FFT(Ex)
    plt.clf()    
    plt.plot([2.0*np.pi/xmax*i for i in range(len(ex))],[np.abs(xx) for xx in np.fft.fft(ex)])
    plt.xlabel(r'$k_x d_{e0}$')
    plt.ylabel(r'$|E_{x}^k|$')
    plt.yscale('log')
    omegape=r'$\,\omega_{pe0}^{-1}$'
    plttitle="t="+str(int(dt*i*10000.0)/10000.0)+omegape
    plt.title(plttitle)
    plt.savefig(datadir+'fftex_'+str(i)+'.png')


from conf import *
i=0

#getting the grid
grid=np.loadtxt(datadir+'grid.out')
#getting number of timesteps in simulation
Nsteps=int(Tfinish/dt)

for i in range(Nsteps):
	print("i=",i)
	try:
		elex=np.loadtxt(datadir+'ele_'+str(i)+'.out',usecols=(0))
		elepx=np.loadtxt(datadir+'ele_'+str(i)+'.out',usecols=(1))
		ex=np.loadtxt(datadir+'ex_'+str(i)+'.out')
		output(datadir,elex,elepx,grid,ex,dt,i,xmax)
		print("Output generated for i=",i)
	except:
		pass
