import ast
T = int(input())
a = []
for i in range(0, T):
    a = list(ast.literal_eval(','.join(input().split())))
    N = a[0]
    C = a[1]
    M = a[2]
    t = 0
    r = N//C
    t += r
    while(r >= M):
        t += (r//M)
        r = (r//M) + (r%M)
    print(t)
