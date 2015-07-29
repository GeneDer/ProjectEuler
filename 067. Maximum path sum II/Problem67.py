##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

import time

initialTime = time.time()

with open('p067_triangle.txt','r') as i:
    lines = i.readlines()

matrix = []
for line in lines:
    matrix.append(line.split())

for i in range(len(matrix)-2,-1,-1):
    for j in range(len(matrix[i])):
        if (int(matrix[i+1][j])>int(matrix[i+1][j+1])):
            matrix[i][j]=int(matrix[i+1][j])+int(matrix[i][j])
        else:
            matrix[i][j]=int(matrix[i][j])+int(matrix[i+1][j+1])
            
print time.time()-initialTime
print matrix[0][0]
