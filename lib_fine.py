import ast
rd=list(ast.literal_eval(','.join(input().split())))
dd=list(ast.literal_eval(','.join(input().split())))
if(dd[2] < rd[2]):
    print(10000)
elif(dd[1]<rd[1]):
    print(500*(rd[1]-dd[1]))
elif(dd[0]<rd[0]):
    print(500*(rd[0]-dd[0]))
else:
    print(0)
