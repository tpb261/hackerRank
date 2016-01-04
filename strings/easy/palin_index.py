#!/usr/bin/python3
T=int(input())
for t in range(T):
    s=input()
    L=len(s)
    loc = -1
    xor_r = 0
    for l in range(0, L//2):
        r = ord(s[l])^ord(s[L-l-1])
        xor_r ^= r
        if(r):            
            loc=l
    for k in range(l+1, L//2):
        r = ord(s[k])^ord(s[L-k-1])
        xor_r ^= r
    if(-1 != loc):
        if(1 == L%2 and ord(s[loc]) != xor_r ^ord(s[L//2])):
            loc = L-loc-1
        elif(0 == L%2):
            if(loc < L//2):
                mid = s[L//2]
                c = s[loc]
                if(xor_r != ord(mid) ^ ord(c)):
                    loc = L-loc-1
    print(loc)
