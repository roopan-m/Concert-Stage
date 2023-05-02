import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

row = 10
column = 30
currentArray = np.zeros((row, column))
currentArray[:,0] = 1
print('\nHEAT DIFFUSION SIMULATION\n')
nextg= np.zeros((row, column))

nextArray = currentArray.copy()

for timestep in range(1000):
    for r in range(1, row-1):
        for c in range(1, column-1):
            nextArray[r, c] = round(0.1 * currentArray[r-1:r+2, c-1:r+2].sum() + 0.1 * currentArray[r, c], 2)
    currentArray = nextArray.copy()

for i in range(row):
    for y in range(column):
        print(round(nextArray[i, y], 2), end=' ')
    print()

ax = plt.axes()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_aspect("equal")
ax.set_facecolor("black")



#for i in range(row):
    #for y in range(column):
        #if nextg[i, y] > 0:
            #circle = plt.Circle([i, y], 10, color='white', alpha=1 + round(nextg[i, y], 2))
            #ax.add_patch(circle)

#plt.show()





