import ast
N = int(input())
a = list(ast.literal_eval(','.join(input().split())))
a.sort()
k = 0
while (k<N and a[k] > 0):
    print(N-k)
    for i in range(N-1, k-1, -1):
        if(a[i] <= a[k]):
            break
    k = i+1
        
