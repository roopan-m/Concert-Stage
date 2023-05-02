import numpy as np

list = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]])

sX = 1
sY = 1
print(list[sX-1:sX+2, sY-1:sY+2])
print(list[sX, sY])

