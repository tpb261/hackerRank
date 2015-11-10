#/usr/bin/python3

def isPrime(num):
    if(num%2==0):
        return False
    root=int(num**0.5+0.5)
    for i in range(3, root+1, 2):
        if(num%i==0):
            return False
    return True

T=int(input())
for i in range(0, T):
    N=int(input())
    if(N==11 or N==13 or isPrime(N)):
        print(N)
    else:
        l=N-2 if (N%2==1) else N-3
        for n in range(l, int(N**0.5+0.5), -1):
            if(N%n==0 and isPrime(n)):
                fact = n
                break
        print(fact)
