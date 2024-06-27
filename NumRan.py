import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

np.random.seed(19690901)
data = np.random.random((900, 50, 200))
data1 = np.random.random((900, 50, 200))
data2 = np.random.random((900, 50, 200))

fig, (ax, az, ay) = plt.subplots(3, 1, facecolor='k')

plt.subplots_adjust(hspace=0.01)
for ax1 in (ax, az, ay):
    ax1.set_aspect('auto')
    ax1.axis('off') 

for i in range(len(data)):
    ax.cla()
    az.cla()
    ay.cla()
    ax.imshow(data[i], cmap='Greens')
    az.text(65, 30, 'َ( ALLAH )', color='white', fontsize=20, fontweight='bold')
    az.imshow(data1[i], cmap='Greys')
    ay.imshow(data2[i], cmap='Reds')
    plt.pause(0.1)
