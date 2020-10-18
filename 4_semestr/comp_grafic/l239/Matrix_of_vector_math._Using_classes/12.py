class Matrix3x3:
    def __init__(self, x, y, z):
        self.x = Vector3(x.x,x.y,x.z)
        self.y = Vector3(y.x,y.y,y.z)
        self.z = Vector3(z.x,z.y,z.z)
    def __str__(self):
        return "((%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f))"%((self.x).x,(self.x).y,(self.x).z, (self.y).x,(self.y).y,(self.y).z, (self.z).x,(self.z).y,(self.z).z)
    def I(self):
        x = Vector3(1,0,0)
        y = Vector3(0,1,0)
        z = Vector3(0,0,1)
        return Matrix3x3(x,y,z)
    def xR(self,n):
        self.x = self.x.xR(n)
        self.y = self.y.xR(n)
        self.z = self.z.xR(n)
        return self
    def plusM(self,matr2):
        self.x = self.x.plusV(matr2.x)
        self.y = self.y.plusV(matr2.y)
        self.z = self.z.plusV(matr2.z)
        return self
    def minusM(self,matr2):
        self.x = self.x.minusV(matr2.x)
        self.y = self.y.minusV(matr2.y)
        self.z = self.z.minusV(matr2.z)
        return self

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
    def minusV(self,vec2):
        return Vector3((self.x - vec2.x), (self.y - vec2.y), (self.z - vec2.z))
    def dotV(self,vec2):
        return (self.x * vec2.x + vec2.y * self.y + self.z * vec2.z)
    def xV(v1, vec2):
        return Vector3((v1.y * vec2.z - vec2.y * v1.z), (vec2.x * v1.z - v1.x * vec2.z), (v1.x * vec2.y - vec2.x * v1.y))
