import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imageio
from skimage.io import imread_collection
import os

for i in range(4):
	for j in range(6):
		data = pd.read_csv('%d-%d' % (i, j), header=None)
		for k, v in data[data[0] != 'spin component  2'].groupby((data[0] == 'spin component  2').cumsum()):
			print('Main sequence in %d' % i)
			print(f'[group {k}]')
			pre = v[v[0] != '--']
			matrix = pre[0].str.split(' +', expand=True).drop([0], axis=1).to_numpy(dtype=float)
			print(matrix)
			plt.imshow(matrix)
			plt.title('Iteration %d' % k)
			plt.colorbar()
			plt.savefig('%d-%d-%d.png' % (i, j, k), dpi=720, bbox_inches='tight')
			plt.close("all")
			print('Complete')

os.system("mkdir IMAGES")
os.system("mv *.png IMAGES")

for k in range(4):
	for l in range(6):
		seq = imread_collection('IMAGES/%d-%d-*.png' % (k, l), conserve_memory=True)
		imageio.mimsave('IMAGES/%d-%d.gif' % (k, l), seq, duration=2)