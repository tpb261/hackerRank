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
    #print(rot)
    for j in range(l, dim[1]-l-1):
        rot.append(a[j*dim[0]+dim[0]-l-1])
    #print(rot)
    c=a[(dim[1]-l-1)*dim[0]+l+1:(dim[1]-l-1)*dim[0]+dim[0]-l]
    c.reverse()
    rot.extend(c)
    #print(rot)
    for j in range(dim[1]-l-1, l, -1):
        rot.append(a[j*dim[0]+l])
    #print (rot)
#    for j in range(0, dim[1]):
#        print(*a[j*dim[0]:(j+1)*dim[0]], sep=' ')

    r = dim[2]%len(rot)
    rot = rot[r:]+rot[0:r]
    #print(rot)
    #top row copied
    a[l*dim[0]+l:l*dim[0]+(dim[0]-l)]=rot[:dim[0]-2*l]
    k=dim[0]-2*l
    #print(k)
#    for j in range(0, dim[1]):
#        print(*a[j*dim[0]:(j+1)*dim[0]], sep=' ')
    #copy right column
    for j in range(l+1, dim[1]-l-1):
        #print ("j=%d, k=%d l=%d a[%d]" %(j, k, l, j*dim[0]+dim[0]-l-1))
        a[j*dim[0]+dim[0]-l-1] = rot[k]
        k+=1
#    k=k+(dim[1]-l-1-l)
    #print(k)
#    for j in range(0, dim[1]):
#        print(*a[j*dim[0]:(j+1)*dim[0]], sep=' ')
    c= rot[k:k+dim[0]-l*2]
    #print(c)
    c.reverse()
    #print(c)
    a[(dim[1]-l-1)*dim[0]+l:(dim[1]-l-1)*dim[0]+dim[0]-l]=c
    k=k+dim[0]-l*2
    #print (k)
#    for j in range(0, dim[1]):
#        print(*a[j*dim[0]:(j+1)*dim[0]], sep=' ')
    for j in range(dim[1]-l-2, l, -1):
        a[j*dim[0]+l]=rot[k]
        #print ("j=%d, k=%d l=%d a[%d]" %(j, k, l, j*dim[0]+l))
        k+=1
for j in range(0, dim[1]):
    print(*a[j*dim[0]:(j+1)*dim[0]], sep=' ')

