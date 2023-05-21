import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from classes import Lights, Smoke 
from matplotlib.patches import Ellipse, Circle
import sys
import random

################################################# VARIABLES
l_origin_1 = [] 
l_origin_2 = []
l_origin_3 = []
l_colour_1 = []
l_colour_2 = []
l_colour_3 = []
drumColour = []
guitarColour = []

################################################## FUNCTIONS
def buildGraph(ax0, ax1):
    ax0.set_aspect("equal")
    ax0.fill([0,500,500,0],[0,0,50,50], color="black")
    ax1.fill([0,500,500,0],[0,0,500,500], color="black")
    plt.suptitle("STAGEVIEW", fontsize="18")
    plt.xlim(-30, 530)
    ax1.set_aspect("equal")

def readData():
    if len(sys.argv) <= 1:
        print("Error: Missing Argument")
        exit()
    with open(str(sys.argv[1]), 'r') as f:
        data = f.readlines()
        f.close()
    
    setup = False
    for line in data:
        if setup == False:
            splitLines = (line.strip(' \n').split(', '))
            l_colour_1.append(str(splitLines[0]))
            l_colour_2.append(str(splitLines[1]))
            l_colour_3.append(str(splitLines[2]))
            drumColour.append(str(splitLines[3]))
            guitarColour.append(str(splitLines[4]))
            setup = True
        else:
            splitLines = (line.strip(' \n').split(','))
            l_origin_1.append(int(splitLines[0]))
            l_origin_2.append(int(splitLines[1]))
            l_origin_3.append(int(splitLines[2]))


def plotInstruments(ax1):

    # DRUMS
    ellipse = Ellipse([100,100], 60, 20, color='lightgrey', zorder=3)
    ax1.add_patch(ellipse)
    ellipse = Ellipse([100,60], 60, 20, color=drumColour[0], zorder=3)
    ax1.add_patch(ellipse)
    ellipse = Ellipse([200,110], 60, 20, color='lightgrey', zorder=3)
    ax1.add_patch(ellipse)
    ellipse = Ellipse([200, 80], 60, 20, color=drumColour[0], zorder=3)
    ax1.add_patch(ellipse)
    circle = Circle([150, 80], 40, color='lightgrey', zorder=4)
    ax1.add_patch(circle)
    circle = Circle([150, 92], 37, color=drumColour[0], zorder=3)
    ax1.add_patch(circle)

    ax1.fill([69, 130, 130, 69],[60, 60, 100, 100], color=drumColour[0], zorder=2)
    ax1.fill([170, 230, 230, 170], [80, 80, 110, 110], color=drumColour[0], zorder=2)

    ax1.fill([80, 85, 85, 80], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor=drumColour[0])
    ax1.fill([110, 115, 115, 110], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor=drumColour[0])
    ax1.fill([187, 192, 192, 187], [0, 0, 90, 90], color='lightgrey', linewidth=1, edgecolor=drumColour[0])
    ax1.fill([215, 220, 220, 215], [0, 0, 90, 90], color='lightgrey', zorder=1, linewidth=1, edgecolor=drumColour[0])

    #GUITAR
    circle = Circle([370, 70], 40, color=guitarColour[0])
    ax1.add_patch(circle)
    circle = Circle([390, 110], 30, color=guitarColour[0])
    ax1.add_patch(circle)
    circle = Circle([395, 110], 15, color='black', zorder=2)
    ax1.add_patch(circle)
    circle = Ellipse([360, 62], 20, 13, color='white', zorder=3)
    ax1.add_patch(circle)
    ax1.fill([358, 458, 452, 352], [40, 200, 210, 50], color=guitarColour[0])
    ax1.plot([450, 355], [200, 60], color='white')
    ax1.plot([450, 360], [190, 57], color='white')

    #MUSIC
    for i in range(3):
        randX = random.randint(300, 400) 
        randY = random.randint(150, 250)
        noteCenter = [randX,randY]
        ellipse = Ellipse([noteCenter[0] + 1, noteCenter[1]], 20, 10, color=guitarColour[0])
        ax1.add_patch(ellipse)
        ax1.fill([noteCenter[0] + 7, noteCenter[0] + 10.5, noteCenter[0] + 10.5, noteCenter[0] + 7],[noteCenter[1], noteCenter[1], noteCenter[1] + 25, noteCenter[1] + 25], color=guitarColour[0])

    for i in range(3):
        randX = random.randint(50, 150) 
        randY = random.randint(150, 250)
        noteCenter = [randX,randY]
        ellipse = Ellipse([noteCenter[0] + 1, noteCenter[1]], 20, 10, color=drumColour[0])
        ax1.add_patch(ellipse)
        ax1.fill([noteCenter[0] + 7, noteCenter[0] + 10.5, noteCenter[0] + 10.5, noteCenter[0] + 7],[noteCenter[1], noteCenter[1], noteCenter[1] + 25, noteCenter[1] + 25], color=drumColour[0])

    #SMOKE MACHINE
    ax1.fill([0, 20, 20, 0], [0, 0, 70, 70], color='darkgrey', zorder=5)
    ax1.fill([20, 40, 40, 20], [0, 0, 80, 70], color='grey', zorder=5)


###################
################################################## MAIN
###################
def main():
    #Graph Construction
    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]},
                                figsize = (10,10))
    
    #Read in Information for Lights
    readData()

    #Light Construction
    def update(frame):
        ax0.clear()
        ax1.clear()
        buildGraph(ax0, ax1)

        plotLights = Lights(l_origin_1, l_origin_2, l_origin_3, l_colour_1[0], l_colour_2[0], l_colour_3[0], frame, ax0, ax1)
        plotLights.plot()
        plotSmoke = Smoke(frame, ax1)
        plotSmoke.plot()
        plotInstruments(ax1)

    #Animate and update graph through update() 
    animationMain = FuncAnimation(fig, update, interval=100, frames=len(l_origin_1), repeat=False)
    plt.show()

if __name__ == '__main__':
    main()



