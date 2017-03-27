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

    if(n%2==0): n=n+1
    if(m%2==1): m=m+1

    b1 = b2 = True

    if(n<=3 and m>=5):
        n=5
        count = 1
    s=(n+1)//6
    e=(m+1)//6
    
    for i in range(s, e):
        if(i%10 == 1 or i%10 == 6 or i%10==9 or i%10==4):
            continue
        p1=6*i-1
        p2=p1+2
        if(p1<n or p2>m or p1>m or p2<n):
            continue
        b1 = b2 = True
        for j in range(7, 1+int(p1**(1/2))):
            if(p1%j == 0):
                b1=False
                break
        if(b1):
            for j in range(7, 1+int(p2**(1/2))):
                if(p2%j == 0):
                    b2=False
                    break
        count = count + b1*b2
    
    return (count)


#for n in range(3, 100):
#    for m in range(5, 100):
#        print(n, m)

#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
n,m=[999000000, 1000000000]
print(getTwinPrimeCount(n, m))    

