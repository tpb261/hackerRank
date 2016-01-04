#!/usr/bin/python3
T=int(input())
for t in range(T):
    s1 = input()
    s2 = input()
    res = 0
    for c in range(ord('a'), ord('z')+1):
        if(s1.count(chr(c)) > 0 and s2.count(chr(c)) > 0):
            print("YES")
            res = 1
            break
    else:
        print("NO")
