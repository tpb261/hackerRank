T=int(input())
for i in range(0, T):
    N=int(input())
    count = 2 #(N+1, N*(N+1)) and (2*N, 2*N)
    for x in range(2, int(N**0.5+0.5+1)):
        if(0==N%x):
            count+=1
    print(count)
