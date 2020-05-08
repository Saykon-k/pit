def Norm(v):
    vec_len = (v[0]*v[0]+v[1]*v[1]+v[2]*v[2])**0.5
    if vec_len != 0:
        return (v[0]/vec_len,v[1]/vec_len,v[2]/vec_len)
    else:
        return (0,0,0)
print(Norm((3,-3,2)))