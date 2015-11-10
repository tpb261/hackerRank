#!/usr/bin/python3
import ast
import re
T=int(input())
for t in range(T):
    [R, C] = list(ast.literal_eval(','.join(input().split())))
    a=[]
    m=[]
    for r in range(R):
        a.append(str(input()))
    
    [r, c] = list(ast.literal_eval(','.join(input().split())))
    pat=re.compile(input())
    for i in range(R-r+1):
        m.append({l.start() for l in pat.finditer(a[i])})

#    print(m)
    for i in range(1, r):
        pat=re.compile(input())
        for j in range(0, R-r+1):
            m[j]=m[j]-{k for k in m[j] if(pat.match(a[i+j][k:]) is None)}
#            print(m[j])

    yes=0
    for l in m:
        if(len(l)>0):
            yes=1
            break
    print(["NO", "YES"][yes])
