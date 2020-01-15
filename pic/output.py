"""@package Output
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def full_output(field,epc,ipc,datadir,numstep):
	"""
	Function to output all meaningfull data, may be used to restart simulation
	or for simulation analysis, dumps field, (position,momentum) of particles
	into datadir directory
	"""
	elex=np.zeros(epc.particles.size)
	elepx=np.zeros(epc.particles.size)
	ionx=np.zeros(ipc.particles.size)
	ionpx=np.zeros(ipc.particles.size)
	for i in range(epc.particles.size):
		elex[i]=epc.particles[i].position
		elepx[i]=epc.particles[i].momentum
		ionx[i]=ipc.particles[i].position
		ionpx[i]=ipc.particles[i].momentum
	np.savetxt(datadir+'grid.out',field.grid.get_grid(), delimiter=',')
	np.savetxt(datadir+'ex_'+str(numstep)+'.out',field.get_field(), delimiter=',')
	np.savetxt(datadir+'ele_'+str(numstep)+'.out',np.array(list(zip(elex,elepx))))
	np.savetxt(datadir+'ion_'+str(numstep)+'.out',np.array(list(zip(ionx,ionpx))))


def postprocess(datadir,xe, pex, grid, ex, dt, i,xmax):
	"""
	This function plots a bunch of figures from the raw output files
	"""
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
