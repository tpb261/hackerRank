import ast
N = int(input())
a=[]
a = list(ast.literal_eval(','.join(input().split())))
p=n=z=0
if(len(a) == N):
    for e in a:
        if(e>0):
            p+=1
        elif(e<0):
            n+=1
        else:
            z+=1

if(p+n+z == N):
    print("%1.3f"% (p*1.0/N))
    print("%1.3f"% (n*1.0/N))
    print("%1.3f"% (z*1.0/N))
