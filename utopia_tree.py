import ast
T = int(input())
for i in range(0, T):
    n=int(input())
    p=(n-1)//2
    num = 2**(p+2)-2
    num=num+(1-n%2)
    print(num)
    
