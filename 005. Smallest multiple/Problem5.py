##Written by Gene Der Su at 7/27/2015
##Python verson 2.7.6

maxNumber = 20
productList = [0]*maxNumber
for i in range(2,maxNumber+1):
    tmpProductList = [0]*maxNumber
    tmpNumber=i
    j=2
    while j <= tmpNumber:
        if (tmpNumber%j==0):
            tmpProductList[j-1]+=1
            tmpNumber/=j
        else:
            j+=1
    for k in range(len(productList)):
        if (tmpProductList[k]>productList[k]):
            productList[k]=tmpProductList[k]

smallestMultiple=1
for l in range(len(productList)):
    smallestMultiple*=pow(l+1,productList[l])

print smallestMultiple
