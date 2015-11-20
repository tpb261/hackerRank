#!/usr/bin/python3
T=int(input())
s=set(input())
for t in range(T-1):
    s &= set(input())
print(len(s))
