import sys

n=int(input().strip())
a=list(input().strip().split(' '))
H=list(input().strip().split(' '))
a = [int(i) for  i in a]
m=int(H[0])
hmin=int(H[1])
hmax=int(H[2])
pos=0
found = 0
d=a[-1]-a[0]
if(d==m):
    print(a[0])
elif(0<d<m):
    for i in range(hmin, hmax+1):
        fin1 = a[0]-i+m
        if(hmin<=fin1-a[-1]<=hmax or fin1==a[-1]):
            print(a[0]-i)
            found = 1
            break
if(found == 0):
    i = 0    
    while(i<(n-1)):
        found = 0
        invalid = 0
        d = a[i+1]-a[i]
        print(a[i], a[i+1], d)
        if(d<hmin or d>hmax):
            i=i+1
            continue
        for j in range(i+1, n):
            d = a[j]-a[j-1]
            print(a[i], a[j], d)
            if(d<hmin or d>hmax):
                i = j-1
                invalid = 1
                break
            if(a[j]-a[i]>m):
                invalid = 1
                break
            if(a[j]-a[i]==m):
                found = 1
                invalid = 0
                break
        if(invalid == 1):
            i = i+1
            continue
        if(found == 1 or (a[-1]-a[i]+hmin<=m and a[-1]-a[i]+hmax>=m)):            
            print(a[i])
            break
        i = i+1
if(n == 1):
    print(a[0]+hmax-m)
