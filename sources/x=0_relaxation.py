import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# What must be the y-axis data? Volume or total energy?
matplotlib.rcParams.update({'font.size': 15})

volume = [253.23, 258.90, 259.63, 264.13]
lattic = [9.0974, 9.1740, 9.1835, 9.2942]
cases  = ['NM', 'AFM', 'FM', 'Hubbard \n U']
LDA_EN = [-86.30973888, -99.03540026, -104.73240129,
		  -106.23610840, -105.21257555, -102.70455166,
		  -99.37739145, -95.68899576, -91.93282589,
		  -88.30017367, -84.91707526, -81.83141844, -79.02956261]
GGA_EN = [-70.51657338, -84.93925968, -92.02465038,
		  -94.69003330, -94.65673633, -93.00499041, 
		  -90.42404663, -87.38917792, -84.20600242,
		  -81.07624929, -78.13316183, -75.43565894, -72.97862685]
fig, axes = plt.subplots(2,
						 sharex=True,
						 figsize=(3, 6))
plt.subplots_adjust(hspace=0)

'''
plt.plot(np.linspace(4, 10, 13), LDA_EN, '-o', 
			 markersize=10, 
			 color='tab:blue',
			 label='LDA')
plt.plot(np.linspace(4, 10, 13), GGA_EN, '-o', 
			 markersize=10, 
			 color='tab:orange',
			 label='GGA')
'''

axes[0].plot(cases, lattic, '-o',
			 markersize=10)
axes[1].plot(cases, volume, '-o',
			 markersize=10)
axes[0].set_ylabel('a [Å]')
axes[1].set_ylabel(r'Volume [Å$^{3}$]')

plt.savefig('relaxation.eps', format='eps', bbox_inches='tight')
plt.show()