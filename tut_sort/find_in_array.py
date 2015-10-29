import ast
V  = int(input())
n  = int(input())
ar = list(ast.literal_eval(','.join(input().split())))
f = 0
for i in range(0, n):
    if(int(ar[i])==V):
        f = 1
        break
if(1 == f):
    print(i)
else:
    print(-1)
