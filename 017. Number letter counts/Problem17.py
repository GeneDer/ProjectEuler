##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6

##one(3) two(3) three(5) four(4) five(4) six(3) seven(5) eight(5) nine(4)
##ten(3) eleven(6)+3 twelve(6)+3 thirteen(8)+3 fourteen(8)+4 fifteen(7)+3
##sixteen(7)+4 seventeen(9)+4 eighteen(8)+3 nineteen(8)+4

##twinty(6) thirty(6) forty(5) fifty(5) sixty(5) seventy(7) eighty(6) ninety(6)


import time

def oneToNineteen(n):
    count = 0
    ones = n%10
    if (n/10==1):
        if ((ones==4)|(ones==6)|(ones==7)|(ones==9)):
            count=4
        else:
            count=3
            
    if ((ones==1)|(ones==2)|(ones==6)):
        return count + 3
    elif ((ones==4)|(ones==5)|(ones==9)):
        return count + 4
    elif (ones==0):
        return count
    else:
        return count + 5
        
def multipleOfTen(n):
    if (n == 7):
        return 7
    elif ((n==4)|(n==5)|(n==6)):
        return 5
    else:
        return 6
    

initialTime = time.time()

numberOfLetters=11
for i in range(1,1000):
    hundreds = i / 100
    tens = i%100
    if (hundreds!=0):
        numberOfLetters += 10 + oneToNineteen(hundreds)
        if (tens==0):
            numberOfLetters -=3
    if (tens>19):
        numberOfLetters += multipleOfTen(tens/10) + oneToNineteen(tens%10)
    else:
        numberOfLetters += oneToNineteen(tens)

print time.time()-initialTime
print numberOfLetters
