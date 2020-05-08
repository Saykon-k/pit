def MminusM(m1,m2):
    m1 = list(m1)
    m2 = list(m2)
    for i in range(3):
        m1[i] = VminusV(m1[i],m2[i])
    return tuple(m1)
def VminusV(v1,v2):
    return ((v1[0]-v2[0]),(v1[1]-v2[1]),(v1[2]-v2[2]))