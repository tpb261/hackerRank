import ast
N = int(input())
if(N>1):
    a = list(ast.literal_eval(','.join(input().split())))
    res = 0
    for i in range(0, N):
        res = res ^ int(a[i])
    print(res)
else:
    a = int(input())
    print(a)
