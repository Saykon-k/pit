def MxV(m1,v1):
    m1 = list(m1)
    v1 = list(v1)
    for i in range(3):
        m1[i] = VxrealV(m1[i],v1)
    return tuple(m1)
def VxrealV(v1,v2):
    return ((v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]))
print((MxV(((2.15 ,3.64, 6.26),(73.25, -45.3, 6.13),(5.89, -2.25, 6.36)),(2.672 ,-78.263, 3.236))))