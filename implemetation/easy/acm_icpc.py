#!/usr/bin/python3
import ast
[N, M] = list(ast.literal_eval(','.join(input().split())))
a=[]
max_S = 0
max_S_ind = 0
for i in range(0, N):
    ip = str(input())
    c=int(ip, 2)
    b=bin(c).count("1")
    a.append((c, b))
#    print(a)
    if(a[i][1] == M ):
        max_S=M
        max_S_ind = N

print 
if(max_S < M):
    for i in range(0, N):
        for j in range(0, i):
            if(a[i][1]+a[j][1] >= max_S):
                S=bin(a[i][0] | a[j][0]).count("1")
                if(max_S == S):
                    max_S_ind += 1
                elif(S>max_S):
                    max_S_ind = 1
                    max_S = S
print(max_S)
print(max_S_ind)
