#!/usr/bin/python3
S=input()
L=len(S)
fr=L**0.5
c=int(fr)
r=int(fr)
if(c*r<L):
    c+=1
    if(c*r<L):
        r+=1
    
print(r, c, r*c, L)
if(int(r)*int(c)<L):
    r+=1
s=""
for j in range(0, c):
    for i in range(0, r):
        if(i*c+j<L):
            s=s+S[j+i*c]
        else:
            break
        print(s)
    s=s+" "
print(s)
