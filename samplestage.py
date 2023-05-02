import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from classes import Lights, Smoke 

################################################# VARIABLES
l_origin_1 = [] #Between 0-500
l_origin_2 = []
l_origin_3 = []
l_colour_1='red'
l_colour_2='blue'
l_colour_3='purple'

################################################## FUNCTIONS
def buildGraph(ax0, ax1):
    ax0.set_aspect("equal")
    ax0.fill([0,500,500,0],[0,0,50,50], color="black")
    ax1.fill([0,500,500,0],[0,0,500,500], color="black")
    plt.suptitle("STAGEVIEW", fontsize="18")
    ax1.set_aspect("equal")

def readData():
    with open('colourMovement.csv', 'r') as f:
        data = f.readlines()
        f.close()

    for line in data:
        splitLines = (line.strip(' \n').split(','))
        l_origin_1.append(int(splitLines[0]))
        l_origin_2.append(int(splitLines[1]))
        l_origin_3.append(int(splitLines[2]))

################################################## MAIN
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

        plotLights = Lights(l_origin_1, l_origin_2, l_origin_3, l_colour_1, l_colour_2, l_colour_3, frame, ax0, ax1)
        plotLights.plot()
        plotSmoke = Smoke(frame, ax1)
        plotSmoke.plot()

    #Animate and update graph through update() 
    animationLight = FuncAnimation(fig, update, interval=500, frames=len(l_origin_1), repeat=False)
    plt.show()

if __name__ == '__main__':
    main()



