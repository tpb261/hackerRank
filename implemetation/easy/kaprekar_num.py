#!/usr/bin/python3
p=int(input())
q=int(input())
L=[]
if(0 == p):
    L=[0]
    p=1
for n in range(p, q+1):
    d=len(str(n))
    s=str(n*n)    
    pref="0"+s[:-d]
    suff="0"+s[-d:]
    c = int(pref)+int(suff)
    if(c==n):
        L.append(n)
if(len(L)>0):
    print (*L, sep=' ')
else:
    print("INVALID RANGE")
