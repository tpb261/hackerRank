#!/usr/bin/python3
import ast
T         = int(input())
for t in range(0, T):
    [B, W]    = list(ast.literal_eval(','.join(input().split())))
    [X, Y, Z] = list(ast.literal_eval(','.join(input().split())))
    tot = 0
    if(Y+Z<X):
        tot  = Y*W
        tot += (Y+Z)*B
    elif(X+Z<Y):
        tot  = X*B
        tot += (X+Z)*W
    else:
        tot  = X*B
        tot += Y*W
    print(tot)
