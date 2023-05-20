import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]},
                              figsize = (10,10))

ax0.set_aspect("equal")
ax0.fill([0,500,500,0],[0,0,50,50], color="black")
circle1 = plt.Circle([250,25],20, color="red")
ax0.add_patch(circle1)
circle1 = plt.Circle([350,25],20, color="blue")
ax0.add_patch(circle1)

ax1.set_aspect("equal")
ax1.fill([0,500,500,0],[0,0,500,500], color="black")
ax1.fill([230,270,270,230],[490,490,500,500], color="red")
ax1.fill([230,270,330,170],[490,490,0,0], color="red")
ax1.fill([330,370,370,330],[490,490,500,500], color="blue")
ax1.fill([330,370,430,270],[490,490,0,0], color="blue")


#INSTRUMENTS

#DRUMS
ellipse = Ellipse([100,100], 60, 20, color='lightgrey', zorder=3)
ax1.add_patch(ellipse)
ellipse = Ellipse([100,60], 60, 20, color='darkgreen', zorder=3)
ax1.add_patch(ellipse)
ellipse = Ellipse([200,110], 60, 20, color='lightgrey', zorder=3)
ax1.add_patch(ellipse)
ellipse = Ellipse([200, 80], 60, 20, color='darkgreen', zorder=3)
ax1.add_patch(ellipse)
circle = Circle([150, 80], 40, color='lightgrey', zorder=4)
ax1.add_patch(circle)
circle = Circle([150, 92], 37, color='darkgreen', zorder=3)
ax1.add_patch(circle)

ax1.fill([69, 130, 130, 69],[60, 60, 100, 100], color='darkgreen', zorder=2)
ax1.fill([170, 230, 230, 170], [80, 80, 110, 110], color='darkgreen', zorder=2)

ax1.fill([80, 85, 85, 80], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor='darkgreen')
ax1.fill([110, 115, 115, 110], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor='darkgreen')
ax1.fill([187, 192, 192, 187], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor='darkgreen')
ax1.fill([215, 220, 220, 215], [0, 0, 90, 90], color='lightgrey', zorder=1, linewidth=1, edgecolor='darkgreen')

#GUITAR

circle = Circle([370, 70], 40, color='darkgreen')
ax1.add_patch(circle)
circle = Circle([390, 110], 30, color='darkgreen')
ax1.add_patch(circle)
circle = Circle([395, 110], 15, color='black', zorder=2)
ax1.add_patch(circle)
circle = Ellipse([360, 62], 20, 13, color='green', zorder=3)
ax1.add_patch(circle)
ax1.fill([358, 458, 452, 352], [40, 200, 210, 50], color='darkgreen')
ax1.plot([450, 355], [200, 60], color='white')
ax1.plot([450, 360], [190, 57], color='white')


#SMOKE MACHINE
ax1.fill([0, 20, 20, 0], [0, 0, 70, 70], color='darkgrey')
ax1.fill([20, 40, 40, 20], [0, 0, 80, 70], color='grey')


plt.suptitle("STAGEVIEW", fontsize="18")
plt.show()


