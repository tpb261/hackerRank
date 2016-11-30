import sys

def getTwins(p1, p3, p7, p9):
    b9 = p9!=0
    b3 = p3!=0
    b7 = p7!=0
    b1 = p1!=0
    for j in range(3, 1+int(p9**(1/2))):
        if(p9%j==0):
            b9=False
            break
    for j in range(3, 1+int(p1**(1/2))):
        if(p1%j==0):
            b1=False
            break
    if(b9):
        for j in range(3, 1+int(p7**(1/2))):
            if(p7%j==0):
                b7=False
                break
    if(b1):
        for j in range(3, 1+int(p3**(1/2))):
            if(p3%j==0):
                b3=False
                break
    return b7*b9 + b9*b1 + b1*b3

def getTwinPrimeCount(n, m):
    count = 0

    if(n<=3):
        count = 2 if(7<=m) else 1
    elif(5<=n):
        count = 1 if(7<=m) else 0

    s=(n+4)//5*5
    e=m//5*5
    if(s%10 == 0): s=s+5
    if(e%10 == 0): e=e-5

    n = n+1 if(n%2==0) else n

    p7=p9=p1=p3=0

    if (s-8>=n): p7=s-8 
    if (s-6>=n): p9=s-6 
    if (s-4>=n): p1=s-4
    if (s-2>=n): p3=s-2
    
    count = count+getTwins(p1, p3, p7, p9)
    
    if( s<=e):
        p7=p9=p1=p3=0
        
        if (e+2<=m): p7=e+2 
        if (e+4<=m): p9=e+4 
        if (e+6<=m): p1=e+6
        if (e+8<=m): p3=e+8

        count = count+getTwins(p1, p3, p7, p9)
    
    for i in range(s, e, 10):
        p7=s+2
        p9=s+4
        p1=s+6
        p3=s+8
        count+getTwins(p1, p3, p7, p9)
    
    print(count)


for n in range(3, 100):
    for m in range(5, 100):
        print(n, m)
        getTwinPrimeCount(n, m)
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]

    

