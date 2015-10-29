import ast
n = int(input())
a = []
if(n>2):
    a.extend(list(str(int(input()))))
    for i in range(0, 1):
        print(*a[i*n:(i+1)*n], sep='')
    a.extend(list(str(int(input()))))
    for i in range(2, n):
        a.extend(list(str(int(input()))))
        b = []
        b.append(int(a[(i-1)*n]))
        for j in range(1, n-1):
            a01 = int(a[(i-2)*n+(j-0)])
            a10 = int(a[(i-1)*n+(j-1)])
            a11 = int(a[(i-1)*n+(j-0)])
            a12 = int(a[(i-1)*n+(j+1)])
            a21 = int(a[(i-0)*n+(j-0)])
            #print(a11, a)
            #print(a10 < a11 and a12<a11)
            #print(a01 < a11)
            #print (a21 < a11)
            #print(a01 < a11 and a10 < a11 and a12 < a11 and a21 < a11)
            if(a01 < a11 and a10 < a11 and a12 < a11 and a21 < a11):
                #print("changing")
                b.append("X")
            else:
                b.append(a11)
        b.append(int(a[(i-1)*n+(n-1)]))
        print(*b, sep='')
    b = a[(n-1)*n:]
    print(*b, sep='')
elif(n == 2):
    a.extend(list(str(int(input()))))
    a.extend(list(str(int(input()))))
    for i in range(0, 2):
        print(*a[i*n:(i+1)*n], sep='')
elif(n==1):
    a.extend(list(str(int(input()))))
    for i in range(0, 1):
        print(*a[i*n:(i+1)*n], sep='')

    

