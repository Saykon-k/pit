def MxR(v,n):
    v = list(v)
    for i in range(3):
        v[i] = VxR(list(v[i]),n)

    return tuple(v)
def VxR(v,n):
    return  (v[0]*n,v[1]*n,v[2]*n)

print(MxR(((2.15 ,3.64, 6.26),(73.25, -45.3, 6.13),(5.89, -2.25, 6.36)),0.5))