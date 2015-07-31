##Written by Gene Der Su at 7/31/2015
##Python verson 2.7.6

import time
import math

initialTime = time.time()

numbers=range(0,10)
order=10**6
lexicgraphicOrder=[]
for i in range(len(numbers)-1,0,-1):
    for j in range(i+1):
        currentOrder=math.factorial(i)*j
        if (currentOrder==order-1):
            order-=currentOrder
            lexicgraphicOrder.append(j)
            break
        elif (currentOrder>order-1):
            order-=(currentOrder-math.factorial(i))
            lexicgraphicOrder.append(j-1)
            break
        if (i==j):
            order-=currentOrder
            lexicgraphicOrder.append(j)
lexicgraphicOrder.append(0)           
permutation=''
for i in range(len(numbers)):
    permutation+=str(numbers[lexicgraphicOrder[i]])
    numbers.remove(numbers[lexicgraphicOrder[i]])


print time.time()-initialTime
print permutation
