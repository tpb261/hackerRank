#!/usr/bin/python3

T=int(input())
for t in range(T):
    s=input()
    l=len(s)
    if(l%2==1):
        print(-1)
        continue
    first=s[:l//2]
    second=s[l//2:]
    chng=0
    for c1 in range(65, 92):
        f1 = first.count(chr(c1))
        s1 = second.count(chr(c1))
        f1 += first.count(chr(c1+32))
        s1 += second.count(chr(c1+32))
        chng += abs(f1-s1)
    print(chng//2)
