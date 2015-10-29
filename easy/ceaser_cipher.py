import ast
import re
N = int(input())
a = str(input())
inc = int(input()) % 26
ascA = ord('A')
asca = ord('a')
ascZ = ord('Z')
ascz = ord('z')
b=[]
for i in range(0, N):    
    ascc = ord(a[i])
    if(asca<=ascc<=ascz or ascA<=ascc<=ascZ):
        if(ascA<=ascc<=ascZ):
            ascb = ascA
        elif(asca<=ascc<=ascz):
            ascb = asca
        ascc += (26 - ascb + inc)
        ascc %= 26
        ascc += ascb
    b.append(chr(ascc))
print(*b, sep='')
