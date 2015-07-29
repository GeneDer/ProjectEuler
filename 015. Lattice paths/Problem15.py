##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

import time

initialTime = time.time()

maxNumber=20
matrix=[[1]*maxNumber]*maxNumber

for i in range(1,maxNumber):
    for j in range(1,maxNumber):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

numberOfPath=2*sum(matrix[maxNumber-1])
print time.time()-initialTime
print numberOfPath
