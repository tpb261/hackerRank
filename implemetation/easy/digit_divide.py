import ast
T = int(input())
for i in range(0, T):
    N=int(input())
    c = 0
    S=str(N)
    for ch in S:        
        d=int(ch)
        if(d>0 and 0==N%d):
            c+=1
    print(c)
