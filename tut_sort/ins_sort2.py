import ast
N = int(input())
if(1 == N):
    a=int(input())
    print(a)        
elif(1 <= N):
    a = list(ast.literal_eval(','.join(input().split())))
    for i in range(1, N):
        t = a[i]
        l = i
        for j in range(i-1, -1, -1):
            if(a[j]>a[i]):
                l = j
            else:
                break;
        a[l+1:i+1]=a[l:i]
        a[l] = t
        print(*a, sep=' ')
#    print(*a, sep=' ')
