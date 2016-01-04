#!/usr/bin/python3
s1=input()
s2=input()
c1 = 0
for c in range(ord('a'), ord('z')+1):
    c1 += abs(s1.count(chr(c))-s2.count(chr(c)))
print(c1)
