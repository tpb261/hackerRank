import ast
T = int(input())
for i in range(0, T):
    n=int(input())
    if( n>0):
        n &= 0xFFFFFFFF
    print (0xFFFFFFFF^n)
