import ast
s = input()
h = []
ascA = ord('A')
ascZ = ord('Z')
asca = ord('a')
ascz = ord('z')
t = 0
for i in range(0, 26):
    h.append(1);
for c in s:
    ascc = ord(c)
    if(ascA<=ascc<=ascZ):
        asc = ascc-ascA
    elif (asca<=ascc<=ascz):
        asc = ascc-asca
    else:
        asc=-1
    if(asc>=0):
        if(h[asc]):
            t+=1
            if(t==26):
                break
            h[asc]=0
if(t==26):
    print("pangram")
else:
    print("not pangram")
