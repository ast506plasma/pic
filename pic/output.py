"""@package Output
"""
import numpy as np

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
	np.savetxt(datadir+'ex_'+str(numstep)+'.out',field.ex, delimiter=',')
	np.savetxt(datadir+'ele_'+str(numstep)+'.out',np.array(list(zip(elex,elepx))))
	np.savetxt(datadir+'ion_'+str(numstep)+'.out',np.array(list(zip(ionx,ionpx))))
