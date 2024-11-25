# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:50:22 2024

@author: sp1v23
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from the table
bird_varieties = ['Caribro', 'Chabro', 'Krishibro']
parameters = ['Moisture', 'Protein', 'Fat', 'Ash']

# Mean values and standard deviations (assuming you have this data in a suitable format)
means = [[74.81, 19.90, 3.80, 2.57],
         [76.39, 17.67, 3.25, 1.73],
         [75.64, 18.65, 3.51, 2.17]]

std_devs = [[0.557, 0.33, 0.05, 0.07],
            [0.557, 0.39, 0.06, 0.02],
            [0.557, 0.30, 0.06, 0.07]]

# Create the bar plot
x = np.arange(len(parameters))
width = 0.2

colors = ['blue', 'green', 'red']

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, means[0], width, label='Caribro', yerr=std_devs[0], capsize=10, color=colors[0])
rects2 = ax.bar(x, means[1], width, label='Chabro', yerr=std_devs[1], capsize=10, color=colors[1])
rects3 = ax.bar(x + width, means[2], width, label='Krishibro', yerr=std_devs[2], capsize=10, color=colors[2])

# Add labels, title, and legend
ax.set_ylabel('Parameter %')
ax.set_title('Comparision of Bird Varieties')
ax.set_xticks(x)
ax.set_xticklabels(parameters)
ax.legend()

# Adjust layout
fig.tight_layout()
plt.savefig('bird_varieties_plot.png', dpi=300, bbox_inches='tight')
plt.show()



















