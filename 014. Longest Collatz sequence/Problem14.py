##Written by Gene Der Su at 7/28/2015
##Python verson 2.7.6
##still have room for improvement, but its the fastest I can do as of today.

import time

def collatz(n):
    if (n%2==0):
        return n/2
    else:
        return 3*n + 1

initialTime = time.time()

maxNumber=1000000
collatzTable={'1':1, '2':2}
for i in range(3,maxNumber+1,2):
    count = 0
    tmpNumberList=[i]
    while (tmpNumberList[len(tmpNumberList)-1]>1):
        tmpNumberList.append(collatz(tmpNumberList[len(tmpNumberList)-1]))
        if str(tmpNumberList[len(tmpNumberList)-1]) in collatzTable:
            for j in range(len(tmpNumberList)-1):
                collatzTable[str(tmpNumberList[j])] = len(tmpNumberList) - j - 1 + collatzTable[str(tmpNumberList[len(tmpNumberList)-1])]
            break
    
        
        
print time.time()-initialTime
##print collatzTable
print max(collatzTable, key=collatzTable.get)
