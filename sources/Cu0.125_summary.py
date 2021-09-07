import matplotlib.pyplot as plt
#from brokenaxes import brokenaxes
from matplotlib.gridspec import GridSpec
import numpy as np
import pandas as pd
import glob
import os

# NM, AFM, FM
TOTEN		= [-190.32341429, -192.13822894, -191.95346797]
U			= [0.0, 2.0, 4.0, 6.0]
indirect 	= [0.902, 1.529, 2.08, 2.476] # 2.476, 2.793, 2.835 for U = 6, 8, 10 eV
direct 		= [1.22154, 2.11531, 2.73939, 3.13206, 3.29131, 3.38174]
kpoints		= [i for i in range(4, 20, 4)]
en			= [i for i in range(200, 750, 50)]
Cu_O		= [1.99958, #7
			   2.15050, #15
			   2.07783, #19
			   2.04953, #23
			   2.23369, #27
			   2.01438] #32
Ni_O		= [1.99364,
			   1.99364,
			   2.06759,
			   2.06144,
			   2.06759,
			   2.06144]

plt.figure(figsize=(10, 8))
plt.rcParams.update({'font.size': 24})
linewidth 	= 10
marker_size = 20

def plot_bandU():
	fig, axes = plt.subplots(figsize=(5, 5))
	plt.subplots_adjust(hspace=0)
	
	'''
	axes.plot(U, [x1-x2 for (x1,x2) in zip(direct, indirect)], 
			 '-o', 
			 lw=linewidth, 
			 markersize=marker_size,
			 color='tab:blue')
	axes.set_ylabel(r'$\Delta$E = E$_{direct}$ - E$_{indirect}$ [eV]', color='tab:blue')
	axes1 = axes.twinx()
	'''
	axes.plot(U, indirect, '-o', markersize=marker_size)

	axes.set_ylabel('Indirect gap [eV]')
	axes.set_xlabel(r'Hubbard $U$ [eV]')
	axes.set_xticks([0, 2, 4, 6])
	#axes.tick_params(axis='y', labelcolor='tab:blue')
	#axes1.tick_params(axis='y', labelcolor='tab:orange')

def plot_toten():
	plt.plot(['NM', 'AFM', 'FM'], TOTEN,
			  '-o', 
			  lw=linewidth, 
			  markersize=marker_size)
	#plt.yticks([])
	plt.ylabel('Total energy [eV]')

def plot_bonding_length():
	plt.plot(['7', '15', '19', '23', '27', '32'], Cu_O, 
			  '-o', 
			  label='Cu-O', 
			  lw=linewidth, 
			  markersize=marker_size)
	plt.plot(['7', '15', '19', '23', '27', '32'], Ni_O, 
			  '-o', 
			  label='Ni-O', 
			  lw=linewidth, 
			  markersize=marker_size)
	plt.xlabel('Oxygen number [a.u.]')
	plt.ylabel('Bonding length [Å]')
	plt.legend()

def plot_kpoints_cutoff():
	files 	= glob.glob('functionals/*.csv')
	
	kpoints	= [i for i in range(4, 20, 4)]
	en		= [i for i in range(200, 750, 50)]

	fig, axes = plt.subplots(2, 1, figsize=(10, 15))
	plt.subplots_adjust(wspace=0)

	for i in range(len(files)) :
		data 	= pd.read_csv(files[i], header=None)[1]
		func 	= os.path.basename(files[i])
		arr  	= data.values.reshape(len(kpoints), len(en))

		axes[0].plot(en, arr[i], '-o', 
					 label=func[:-4],
					 lw=linewidth, 
			 		 markersize=marker_size)
		
		axes[1].plot(kpoints, arr.T[4], '-o', 
					 label=func[:-4],
					 lw=linewidth, 
					 markersize=marker_size)
	axes[0].set_ylabel('Total energy [eV]')
	axes[0].set_xlabel('Cutoff energry [eV]')
	axes[1].set_xlabel('k-points [a.u.]')
	axes[1].set_ylabel('Total energy [eV]')
	plt.legend()

plot_bandU()
plt.savefig('bandU.eps', bbox_inches='tight')
