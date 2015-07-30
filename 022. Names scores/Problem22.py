##Written by Gene Der Su at 7/30/2015
##Python verson 2.7.6

import time
import math

initialTime = time.time()

names = []
with open('p022_names.txt','r') as i:
    lines = i.readlines()
    names=sorted(lines[0].split(','))

nameScores=0
for i in range(len(names)):
    tmpScore=0
    for j in range(1,len(names[i])-1):
        tmpScore+=ord(names[i][j])-64
    nameScores+=(i+1)*tmpScore
    
print time.time()-initialTime
print nameScores
