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
    def norm(self):
        selfec_len = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
        if selfec_len != 0:
            return Vector3(self.x/selfec_len,self.y/selfec_len,self.z/selfec_len)
        else:
            return Vector3(0,0,0)
    def xR(self, n):
        return Vector3(self.x * n, self.y * n, self.z * n)
    def plusV(self,vec2):
        return Vector3((self.x + vec2.x), (self.y + vec2.y), (self.z + vec2.z))