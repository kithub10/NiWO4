import matplotlib.pyplot as plt

# This source plots the total energies 
# for different configurations in Cu0.25Ni0.75WO4

MM_TOTEN = [-366.47088734, -366.51413398, -366.54900073, -366.40231912, -366.47848703]
NM_TOTEN = [-377.24108308, -377.23856688, -377.25475177, -377.26921301, -377.23450246]
configs = ['Config 1', 'Config 2', 'Config 3', 'Config 4', 'Config 5']
en = []

fig, ax1 = plt.subplots(figsize=(5, 5))

ax1.plot(configs, NM_TOTEN, marker='o', label='Non Magnetic', color='tab:blue')
ax2 = ax1.twinx()
ax2.plot(configs, MM_TOTEN, marker='o', label='Antiferromagentic', color='tab:orange')

plt.xlabel('Configurations [a.u.]')
ax1.set_ylabel('Total energy [eV]')

ax1.tick_params(axis='y', labelcolor='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# fig.legend(loc='upper left', bbox_to_anchor=(0.13, 0.88))

plt.savefig('Toten_Cu_0.25.eps', format='eps', bbox_inches='tight')