#!/usr/bin/python3
import re
T=int(input())
for t in range(T):
    s=input()
    strA=re.compile("AA+")
    strB=re.compile("BB+")
    r=sum([l.end()-l.start()-1 for l in strA.finditer(s)])
    r+=sum([l.end()-l.start()-1 for l in strB.finditer(s)])
    print(r)
