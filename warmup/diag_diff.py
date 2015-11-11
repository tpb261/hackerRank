import ast
n = int(input())
a=[]
s1=s2=0
for i in range(0, n):
    a = list(ast.literal_eval(','.join(input().split())))
    if(len(a) == n):
        s1+=a[i]
        s2+=a[n-1-i]
print(abs(s1-s2))
