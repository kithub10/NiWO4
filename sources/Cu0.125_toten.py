import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 17})

titles 		= ['AFM Cu(+1)', 'AFM Cu(-1)']
U		= [2.0, 4.0, 6.0, 8.0]
TOTEN           = [-368.12772672, -367.48263132, -366.94768380, -366.44713703,
                   -368.16233328, -367.51121220, -366.92547899, -366.46818999]
ydata           = []

for i in range(4):
	ydata.append(TOTEN[i] - TOTEN[i+4])

plt.bar(U, ydata)
plt.title(r'$E_{\mu=+3} - E_{\mu=-3}$')
plt.tight_layout()
plt.xticks([2, 4, 6, 8])
plt.xlabel('Hubbard U [eV]')
plt.ylabel('Total energy difference [eV]')
plt.savefig('UbyT.eps', format='eps', bbox_inches='tight')
plt.show()
