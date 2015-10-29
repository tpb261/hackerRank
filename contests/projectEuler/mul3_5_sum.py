T=int(input())
for i in range(0, T):
    n=int(input())
    n3 = min(n//3, (n-1)//3)
    n5 = min(n//5, (n-1)//5)
    n15 = min(n//15, (n-1)//15)
    print(int(n3*(n3+1)*3//2+n5*(n5+1)*5//2-n15*(n15+1)*15//2))
