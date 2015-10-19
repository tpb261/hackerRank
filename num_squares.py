import ast
T = int(input())
for i in range(0, T):
    a = list(ast.literal_eval(','.join(input().split())))
    r1 = int(a[1]**0.5)
    r2 = int(a[0]**0.5)
    if(r2*r2==a[0]):
        print (r1-r2+1)
    else:
        print(r1-r2)

