#!/usr/bin/python3

s[]=["aaabbbb", "cdefghmnopqrstuvw", "cdcdcdcdeeeef"]#input()
odd_count = 0
for c in range(ord('a'), ord('z')+1):
#    print(chr(c), s.count(chr(c)), odd_count)
    if(1 == s.count(chr(c)) % 2):
        odd_count+=1
        if(odd_count > 1):
            break
#print(odd_count)
if(1 >= odd_count):
    print("YES")
else:
    print("NO")

