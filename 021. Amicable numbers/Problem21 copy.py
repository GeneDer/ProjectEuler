##Written by Gene Der Su at 7/29/2015
##Python verson 2.7.6
##taking the proper_divs() directly from rosettacode.org
##Source: http://rosettacode.org/wiki/Proper_divisors#Python:_From_prime_factors

import time
##from math import sqrt
import math
from functools import reduce
from collections import Counter
from itertools import product
 
 
MUL = int.__mul__
 
 
def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]
 
 
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())

def sOD(x):
	s = 1
	for i in range(2, int(math.sqrt(x)) + 1):
		if (x % i == 0):
			s += i
			s += x / i
	return s

def findSum():
	sum = 0
	for i in range(1, 10000):
		x = sOD(i)
		if (sOD(x) == i):
			if (i != x):
				sum += i
	return sum


initialTime = time.time()
##maxNumber = 10000
##amicable=set()
##
##for i in range(2,maxNumber):
##    if i not in amicable:
##        tmpNumber1=sum(proper_divs(i))
##        if (tmpNumber1!=i):
##            tmpNumber2=sum(proper_divs(tmpNumber1))
##            if (i==tmpNumber2):
##                amicable.add(tmpNumber1)
##                amicable.add(tmpNumber2)
##                
##amicableSum=sum(amicable)

amicableSum=findSum()
print time.time()-initialTime
print amicableSum
