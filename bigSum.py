import ast
n = int(input())
a=[]
s=0
a = list(ast.literal_eval(','.join(input().split())))
if(len(a) == n):
    for e in a:
        s=s+e
print(s)
