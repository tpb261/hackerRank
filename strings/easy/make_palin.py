#!/usr/bin/python3
import itertools
T=int(input())
for t in range(T):
    s=input()
    c = 0
    L=len(s)
    for l in range(0, L//2):
        c+=abs(ord(s[l])-ord(s[L-l-1]))
    print(c)
