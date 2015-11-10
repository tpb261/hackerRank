import ast
T = int(input())
for t in range(0, T):
    s = input()
    n = len(s)
    no_funny = 0
    for i in range(1, n//2+1):
        ascc1 = ord(s[i-1])
        ascc2 = ord(s[i])
        ascc3 = ord(s[n-i-1])
        ascc4 = ord(s[n-i])
        if(abs(ascc1-ascc2)!=abs(ascc3-ascc4)):
            no_funny = 1
            break
    if(no_funny==1):
        print("Not Funny")
    else:
        print("Funny")
