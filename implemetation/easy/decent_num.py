import ast
n = int(input())
for i in range(0, n):
    m = int(input())
    num = 0
    l = m-(m%3)
    for j in range(l, -1, -3):
        if(0 == (m-j)%5):
            num=1
            s=""
            for k in range(0, m-j, 5):
                s=''.join(['33333', s])
            for k in range(0, j, 3):
                s=''.join(['555', s])
            print(s)
            break
    if( num == 0):
        print (-1)
