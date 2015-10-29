T=int(input())
for t in range(0, T):
    n=int(input())
    [f1, f2, f3]=[1, 1, 2]
    S=0
    while(f1<=f2<f3<n):
        f1=f2+f3
        f2=f3+f1
        f3=f1+f2
    print((f2-1)//2)
