def MxM(m1,m2):
    m1 = list(m1)
    m2 = list(m2)
    prom = []
    ne_matr = [[],[],[]]
    for i in range(3):
        for l in range(3):
            prom.append(m2[l][i])
        for j in range(3):
            m1[j] = list(m1[j])
            ne_matr[j].append( VxrealV(m1[j],prom))
        prom.clear()
    for i in range(3):
        ne_matr[i] = tuple(ne_matr[i] )
    return tuple(ne_matr)
def VxrealV(v1,v2):
    return ((v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]))
print(MxM(((2.15, 3.64, 6.26),(73.25, -45.3 ,6.13),(5.89, -2.25, 6.36)),((26.672, -3478.263, 23.236),
          (-346.37 ,874.347 ,-734.63),
          (457.27, 9283.36, -27.2678))))