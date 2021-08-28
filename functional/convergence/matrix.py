import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn as sns
import glob
import os
import numpy as np

plt.rcParams.update({'font.size': 20})
files 	= glob.glob('*.csv')
kpoints	= [i for i in range(4, 20, 4)]
en		= [i for i in range(200, 750, 50)]
code 	= 'matrix'

for i in range(len(files)) :
	data 	= pd.read_csv(files[i], header=None)[1]
	func 	= os.path.basename(files[i])

	if code == 'matrix' :
		fig  = plt.subplots(figsize=(12, 8))
		#arr  = data['TOTEN'].values.reshape(len(kpoints), len(en))
		arr  = data.values.reshape(len(kpoints), len(en))
		plt.imshow(arr, 
				   norm=colors.PowerNorm(gamma=0.4),
				   interpolation='nearest',
				   aspect='auto')
		for j in range(len(kpoints)) :
			for k in range(len(en)):
				pass
				#text = plt.text(k, j, '%.3f' % arr[j, k], ha="center", va="center", color="w")
		plt.colorbar()
		plt.xticks(np.arange(len(en)), en)
		plt.yticks(np.arange(len(kpoints)), kpoints)
		plt.title(func[6:-4])
	else :
		data = data.sort_values('ENCUT', ignore_index=True)
		plt.plot(data['ENCUT'], data['Energy'], '-o')
	plt.xlabel('Energy [eV]')
	plt.ylabel(r'$k$-points')
	plt.savefig('%s-scatter.eps' % files[i][:-4], format='eps')
	plt.show()
	plt.close("all")
