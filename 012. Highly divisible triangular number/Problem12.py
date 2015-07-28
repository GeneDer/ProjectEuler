##Written by Gene Der Su at 7/28/2015
##Python verson 2.7.6

import math
import time

initialTime = time.time()

maxNumber=4
with open('grid.txt','r') as i:
    lines = i.readlines()

matrix = []
for line in lines:
    matrix.append(line.split())

maxProduct=0
##checking from left to right
for i in range(len(matrix)):
    for j in range(len(matrix[i])-maxNumber+1):
        tmpProduct=1
        for k in range(maxNumber):
            tmpProduct*=int(matrix[i][j+k])
        if (tmpProduct > maxProduct):
            maxProduct = tmpProduct

##checking from up to down
for i in range(len(matrix)-maxNumber+1):
    for j in range(len(matrix[i])):
        tmpProduct=1
        for k in range(maxNumber):
            tmpProduct*=int(matrix[i+k][j])
        if (tmpProduct > maxProduct):
            maxProduct = tmpProduct

##checking from up left to down right
for i in range(len(matrix)-maxNumber+1):
    for j in range(len(matrix[i])-maxNumber+1):
        tmpProduct=1
        for k in range(maxNumber):
            tmpProduct*=int(matrix[i+k][j+k])
        if (tmpProduct > maxProduct):
            maxProduct = tmpProduct

##checking from down left to up right
for i in range(len(matrix)-maxNumber+1):
    for j in range(maxNumber-1,len(matrix[i])):
        tmpProduct=1
        for k in range(maxNumber):
            tmpProduct*=int(matrix[i+k][j-k])
        if (tmpProduct > maxProduct):
            maxProduct = tmpProduct
        
print time.time()-initialTime
print maxProduct
