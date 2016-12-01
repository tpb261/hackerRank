import sys

n=int(input().strip())
a=list(input().strip().split(' '))
H=list(input().strip().split(' '))
a = [int(i) for  i in a]
ra = [-i for i in reversed(a)]
m=int(H[0])
hmin=int(H[1])
hmax=int(H[2])
d=[j-i for (i, j) in zip(a[:-1], a[1:])]
d=[di if hmin<=di<=hmax else 0 for di in d]
rd=[j-i for (i, j) in zip(ra[:-1], ra[1:])]
rd=[di if hmin<=di<=hmax else 0 for di in rd]
pos=found=0
dists={}
rdists={}

print(d)
print(rd)
for i in range(n-1):
    dists[i]=[0, 1]
    rdists[i]=[0, 1]
    for j in range(i+1):
        if(dists[j][1]==1):
            if(dists[j][0]<m):
                dists[j][0]=dists[j][0]+d[i]
            if(dists[j][0] == m):
                pos = j
                found = 1
                break
            if(d[i] == 0 and dists[j][0]<m):
                dists[j][1]=0                
            if(dists[j][0]>m):
                dists[j][1]=2
                dists[j][0] = dists[j][0]-d[i]
        if(rdists[j][1]==1):
            if(rdists[j][0]<m):
                rdists[j][0]=rdists[j][0]+rd[i]
            if(rd[i] == 0 and rdists[j][0]<m):
                rdists[j][1]=0
            if(rdists[j][0]>m):
                rdists[j][1] = 2
                rdists[j][0] = rdists[j][0]-rd[i]
    print (dists)
    print (rdists)
    if(found == 1):
        break
if(n == 1):
    print("0",a[0]+hmax-m)
elif(found == 1):
    print("1",a[pos])
elif(dists[0][0]+hmax>=m):
    print("2",a[0]+dists[0][0]-m)
elif(rdists[0][0]+hmax>=m):
    print("3", -(ra[0]+rdists[0][0]-m)-m)
else:
    i = n-2
    while(i>0 and dists[i][0]+hmax<m and dists[i][1]==1):
        print(i, a[i], a[i-1], dists[i])
        i=i-1
    if(dists[i][0]+hmax>=m):
        print("4", a[i])
    else:
        print("5", dists[0][0]+hmax-m)
