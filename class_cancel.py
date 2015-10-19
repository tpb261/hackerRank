import ast
T = int(input())
for i in range(0, T):
    b = list(ast.literal_eval(','.join(input().split())))
    N = b[0]
    K = b[1]
    a = list(ast.literal_eval(','.join(input().split())))
    for i in range(0, N):
        if(K>0):
            if(a[i]<=0):
                K-=1
        else:
             break
    if(K):
        print("YES")
    else:
        print("NO")
        
