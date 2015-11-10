import ast
ad=list(ast.literal_eval(','.join(input().split())))
ed=list(ast.literal_eval(','.join(input().split())))
if(ed[2] < ad[2]):
    print(10000)
elif(ed[1]<ad[1] and ed[2]==ad[2]):
    print(500*(ad[1]-ed[1]))
elif(ed[0]<ad[0] and ed[1]==ad[1] and ed[2]==ad[2]):
    print(15*(ad[0]-ed[0]))
else:
    print(0)
