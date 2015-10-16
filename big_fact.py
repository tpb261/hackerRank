def fact(n, f):
    if(n>1):
        return fact(n-1, n*f)
    else:
        return f
    
    
n=int(input())
print(fact(n, 1))
