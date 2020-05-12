class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(%.2f, %.2f, %.2f)"%(self.x,self.y,self.z)
    def len(self):
        selfec_len = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
        if selfec_len != 0:
            return selfec_len
        else:
            return 0
print((Vector3(1,0,0).len()))