#!/usr/bin/python3

T=int(input())
for t in range(T):
    s=input()
    l=len(s)
    if(l%2==1):
        print(-1)
        continue
    first=Counter(s[:l//2])
    second=Counter(s[l//2:])    
    chng=0
    for c1 in range(65, 91):
        if(first[c1]==second[c1]):
            del(first[c1])
            del(second[c1])
            
    for c1 in range(65, 91):
        if(c1 in first.keys()):
            for c2 in range(65, 91):
                if (c2 in second.keys() and first[c1]==second[c2]):
                    chng += 1
                    del(second[c2])
                    del(first[c1])
                    break
    if((len(first)>0 and len(second)==0)\
       or (len(first)==0 and len(second)>0)):
        print(-1)
    else:
        
        print(chng)
