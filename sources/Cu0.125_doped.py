import matplotlib.pyplot as plt
import numpy as np

'''
titles 		= ['AFM Cu(+1)', 'AFM Cu(-1)', 
			   'FM Cu(+1)', 'FM Cu(-1)']
U			= [0.0, 2.0, 4.0, 6.0, 8.0]
magmom		= [-0.600, 0.631, 0.712, -0.791, -0.846, 
			0.576, -0.655, 0.712, 0.780, 0.838, 
			-0.557, 0.664, -0.703, -0.777, -0.837, 
			0.612, -0.621, -0.704, -0.777, 0.845]
'''
'''
CUSPIN
------------------------------------------------------------
titles 		= ['AFM Cu(+3)', 'AFM Cu(-3)', 
			   'FM Cu(+3)', 'FM Cu(-3)']
U			= [0.0, 2.0, 4.0, 6.0, 8.0]
magmom		= [0.577, -0.652, -0.724, 0.780, 0.838, 
			0.577, 0.639, 0.712, -0.791, 0.838, 
			-0.557, -0.621, -0.703, 0.792, -0.837, 
			-0.557, 0.659, 0.728, -0.777, 0.845]
'''
titles 		= ['AFM Cu(+3)', 'AFM Cu(-3)', 
			   'FM Cu(+3)', 'FM Cu(-3)']
U			= [0.0, 2.0, 4.0, 6.0, 8.0]
magmom		= [0.577, -0.652, -0.724, 0.780, 0.838, 
			0.577, 0.639, 0.712, -0.791, 0.838, 
			-0.557, -0.621, -0.703, 0.792, -0.837, 
			-0.557, 0.659, 0.728, -0.777, 0.845]

plt.rcParams.update({'font.size': 17})

fig, axes 	= plt.subplots(4, 1, 
						   sharex=True, 
						   sharey=True,
						   figsize=(10, 8))


plt.rcParams.update({'font.size': 17})

fig, axes 	= plt.subplots(4, 1, 
						   sharex=True, 
						   sharey=True,
						   figsize=(10, 8))

for i in range(4):
	ydata = magmom[5*i:5+5*i]
	if i == 0 or i == 2 :
		axes[i].fill_between(U, ydata, 
  				   		 where=[ydata[j] < np.zeros(5)[j] for j in range(len(ydata))], 
  				   		 facecolor='tab:red',
  				   		 interpolate=True,
  				   		 alpha=0.5)
		axes[i].fill_between(U, ydata,
  				   		 where=[ydata[j] > np.zeros(5)[j] for j in range(len(ydata))], 
  				   		 facecolor='tab:blue',
  				   		 interpolate=True,
  				   		 alpha=0.5)
	else :
		axes[i].fill_between(U, ydata, 
  				   		 where=[ydata[j] > np.zeros(5)[j] for j in range(len(ydata))], 
  				   		 facecolor='tab:red',
  				   		 interpolate=True,
  				   		 alpha=0.5)
		axes[i].fill_between(U, ydata,
  				   		 where=[ydata[j] < np.zeros(5)[j] for j in range(len(ydata))], 
  				   		 facecolor='tab:blue',
  				   		 interpolate=True,
  				   		 alpha=0.5)
	axes[i].plot(U, magmom[5*i:5+5*i], '-o')
	axes[i].set_xticks([0, 2, 4, 6, 8])
	axes[i].set_title(titles[i], loc='center')

plt.tight_layout()
fig.text(0.0, 0.5, r'Magnetization [$\mu_{B}$]', ha='center', va='center', rotation='vertical')
plt.xlabel('Hubbard parameter [eV]')
plt.savefig('UbyM.eps', format='eps', bbox_inches='tight')
plt.show()