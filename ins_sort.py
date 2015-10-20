import ast
N = int(input())
if(1 == N):
    a=int(input())
    print(a)        
elif(1 <= N):
    a = list(ast.literal_eval(','.join(input().split())))
    t = a[N-1]
    for i in range(N-2, -1, -1):
        if(a[i]>=t):
            a[i+1]=a[i]
            print(*a, sep=' ')
        else:
            a[i+1] = t
            print(*a, sep=' ')
            break
    if( 0 == i and a[i] >= t):
        a[0] = t
        print(*a, sep=' ')
