import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

array = [0, 1, 2, 3, 4, 5]
array_y = [6, 4, 3, 6, 4, 6]

fig = plt.figure(0)
plt.ylim(0, 10)
plt.xlim(0, 10)


def update(frame):
    plt.plot(array[frame], array_y[frame], 'b+', markersize=10)
    

animation = FuncAnimation(fig, update, interval=1000, frames=len(array), repeat=False)
plt.show()
    