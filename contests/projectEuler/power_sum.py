#!/usr/bin/python3
T=int(input())
for t in range(T):
    N=int(input())
    s=str(2**N)
    print(sum([s.count(str(i))*i for i in range(1,10)]))
