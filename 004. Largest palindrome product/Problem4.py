##Written by Gene Der Su at 7/27/2015
##Python version 2.7.6

import time

initialTime = time.time()

digit=3
maxNumber=pow(10,digit)-1
maxPalindrome=9
for i in range(maxNumber,1,-1):
    if (i*maxNumber<maxPalindrome):
        break
    for j in range(maxNumber,i-1,-1):
        palindrome = i*j
        if ((palindrome>maxPalindrome)&(str(palindrome)[::-1]==str(palindrome))):
            maxPalindrome=palindrome

print time.time()-initialTime

print maxPalindrome


