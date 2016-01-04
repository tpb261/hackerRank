#!/usr/bin/python3
import itertools
T=int(input())
for t in range(T):
    n=int(input())
    if(n<2):
        print(0)
        continue
    a=int(input())
    b=int(input())
    L=[(0, 0)]
    for i in range(1, n):
        S=[]
        for p in itertools.product(L, [a, b]):
#            print(p)
            S.append((p[0][0]+p[0][1], p[1]))
        L=set(S)
#        print(L)
    print(*sorted(set([p[0]+p[1] for p in L])))
