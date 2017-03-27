#!/bin/python3

import sys


n = int(input().strip())
p = list(map(int, input().strip().split(' ')))

st = 2
lt = 5


stms = sum(p[lt-st:lt])
ltms = sum(p[:lt])
stma = sum(p[lt-st:lt])/st
ltma = sum(p[:lt])/lt

#print(lt, stma, ltma)

for i in range(lt, len(p)):
    stma_1 = stma
    ltma_1 = ltma
    stms = stms + p[i] - p[i-st]
    ltms = ltms + p[i] - p[i-lt]
    stma = stms/st
    ltma = ltms/lt
#    print(i, stms, ltms)
    if(stma>=ltma and stma_1<ltma_1):
        print (i+1, round(stma, 2), round(ltma, 2))
    if(stma<=ltma and stma_1>ltma_1):
        print (i+1, round(stma, 2), round(ltma, 2))
    if(stma_1 == ltma_1 and stma!=ltma):
        print (i+1, round(stma, 2), round(ltma, 2))
        
