import matplotlib.pyplot as plt
import numpy as np
import random

class Lights:
    def __init__(self, xcoords1, xcoords2, xcoords3, color1, color2, color3, frame, ax0, ax1):
        self.color1 = color1
        self.color2 = color2 
        self.color3 = color3
        self.frame = frame
        self.xcoords1 = xcoords1
        self.xcoords2 = xcoords2
        self.xcoords3 = xcoords3
        self.ax0 = ax0
        self.ax1 = ax1
    
    def plot(self):
        circle1 = plt.Circle([self.xcoords1[self.frame],25],20, color=self.color1)
        self.ax0.add_patch(circle1)
        circle1 = plt.Circle([self.xcoords2[self.frame],25],20, color=self.color2)
        self.ax0.add_patch(circle1)
        circle1 = plt.Circle([self.xcoords3[self.frame],25],20, color=self.color3)
        self.ax0.add_patch(circle1)

        opacityRandom = random.random()
        self.ax1.fill([self.xcoords1[self.frame]-15, self.xcoords1[self.frame]+15, self.xcoords1[self.frame]+50, self.xcoords1[self.frame]-50], [500, 500, 0, 0], color=self.color1, alpha=opacityRandom)
        opacityRandom = random.random()
        self.ax1.fill([self.xcoords2[self.frame]-15, self.xcoords2[self.frame]+15, self.xcoords2[self.frame]+50, self.xcoords2[self.frame]-50], [500, 500, 0, 0], color=self.color2, alpha=opacityRandom) 
        opacityRandom = random.random()
        self.ax1.fill([self.xcoords3[self.frame]-15, self.xcoords3[self.frame]+15, self.xcoords3[self.frame]+50, self.xcoords3[self.frame]-50], [500, 500, 0, 0], color=self.color3, alpha=opacityRandom)
    

class Smoke: 

    def __init__(self, frame, ax1):
        self.frame = frame
        self.ax1 = ax1

    def plot(self):
        row = 10
        column  = 40
        currentArray = np.zeros((row, column))
        nextArray = np.zeros((row, column))
        currentArray[5:9,0] = 1

        for i in range(row):
            for y in range(column):
                print(round(currentArray[i, y], 2), end=' ')
            print()

        rowValues = np.linspace(0, 80, row)
        columnValues = np.linspace(0, 480, column) 

        #Cell Construction
        for timestep in range(self.frame):

            for step in range(10):
                for r in range(1, row-1):
                    for c in range(1, column-1):
                        nextArray[r, c] = round(0.15 * currentArray[r-1:r+2, c-1:c+2].sum() + 0.1 * currentArray[r, c], 3)
                    nextArray[5:9,0] = 1
                currentArray = nextArray.copy()

        for i in range(row):
            for y in range(column):
                print(round(nextArray[i, y], 2), end=' ')
            print()

        #Create Circles
        for i in range(row):
            for y in range(column):
                rand = np.random.randint(5, 10, 2)
                if not nextArray[i, y] > 1:
                    circle = plt.Circle([columnValues[y]+rand[0], rowValues[i]+rand[1]], 4, color='white', alpha=nextArray[i, y])
                else: 
                    circle = plt.Circle([columnValues[y]+rand[0], rowValues[i]+rand[1]], 4, color='white', alpha=1)

                self.ax1.add_patch(circle)

        

            


    



