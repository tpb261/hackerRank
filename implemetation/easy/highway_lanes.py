import ast
t = list(ast.literal_eval(','.join(input().split())))
T = t[1]
N = t[0]
a = list(ast.literal_eval(','.join(input().split())))
for i in range(0, T):
    m=3
    t = list(ast.literal_eval(','.join(input().split())))
    for l in range(t[0], t[1]+1):
        if(a[l] == 1):
            m =1
            break
        elif (a[l]<m):
            m=a[l]
    print(m)

