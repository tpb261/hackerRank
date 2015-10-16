import ast
dim = list(ast.literal_eval(','.join(input().split())))
t=dim[0]
dim[0]=dim[1]
dim[1]=t
a=[]
for i in range(0, dim[1]):
    b = list(ast.literal_eval(','.join(input().split())))
    a.extend(b)
for l in range(0, int(dim[0]/2) if dim[0]<dim[1] else int(dim[1]/2)):
    rot=a[l*dim[0]+l:l*dim[0]+(dim[0]-l)-1]
    print(rot)
    for j in range(l, dim[1]-l-1):
        rot.append(a[j*dim[0]+dim[0]-l-1])
    print(rot)
    c=a[(dim[1]-l-1)*dim[0]+l+1:(dim[1]-l-1)*dim[0]+dim[0]-l]
    c.reverse()
    rot.extend(c)
    print(rot)
    for j in range(dim[1]-l-1, l, -1):
        rot.append(a[j*dim[0]+l])
    print (rot)

    r = dim[2]%len(rot)
    rot = rot[r:]+rot[0:r]
    print(rot)
    a[l*dim[0]+l:l*dim[0]+(dim[0]-l)-1]=rot[:dim[0]-1-2*l]
    k=dim[0]-1-2*l
    print(k)
    for j in range(l, dim[1]-l-1):
        a[j*dim[0]+dim[0]-l-1] = rot[j+k]
    k=k+(dim[1]-l-1-l)
    print(k)
    c= rot[k:k+dim[0]-l]
    print(c)
    c.reverse()
    a[(dim[1]-l-1)*dim[0]+l:(dim[1]-l-1)*dim[0]+dim[0]-l]=c
    k=k+dim[0]-l
    print (k)
    for j in range(dim[1]-l-2, l+1, -1):
        a[j*dim[0]+l]=rot[k+1]
        k+=1
    for j in range(0, dim[1]):
        print(a[j*dim[0]:(j+1)*dim[0]])
