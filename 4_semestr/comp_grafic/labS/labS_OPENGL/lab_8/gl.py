import math
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(%.2f, %.2f, %.2f)"%(self.x,self.y,self.z)
    def len(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def norm(self):
        if self.len() != 0:
            leng = self.len()
            self.x = self.x/leng
            self.y = self.y/leng
            self.z = self.z/leng
            return self
        else:
            return self
    def xR(self, n):
        x = self.x * n
        y = self.y * n
        z = self.z * n
        return vector(x,y,z)
    def plusV(self,vect):
        x = self.x + vect.x
        y = self.y + vect.y
        z = self.z + vect.z
        return vector(x,y,z)
    def minusV(self,vect):
        x = self.x - vect.x
        y = self.y - vect.y
        z = self.z - vect.z
        return vector(x,y,z)
    def dotV(self,vect):
        temp = self.x * vect.x + self.y * vect.y + self.z * vect.z
        return temp
    def xV(self,vect):
        x = self.y*vect.z-self.z*vect.y
        y = -(self.x*vect.z-self.z*vect.x)
        z = self.x*vect.y-self.y*vect.x
        return vector(x,y,z)
    
class matr3x3:
    def __init__(self, a, b, c):
        self.a = vector(a.x,a.y,a.z)
        self.b = vector(b.x,b.y,b.z)
        self.c = vector(c.x,c.y,c.z)
        self.column1 = vector(a.x,b.x,c.x)
        self.column2 = vector(a.y,b.y,c.y)
        self.column3 = vector(a.z,b.z,c.z)
    def __str__(self):
        return "((%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f))"%((self.a).x,(self.a).y,(self.a).z, (self.b).x,(self.b).y,(self.b).z, (self.c).x,(self.c).y,(self.c).z)
    def I():
        a = vector(1,0,0)
        b = vector(0,1,0)
        c = vector(0,0,1)
        return matr3x3(a,b,c)
    def xR(self,n):
        a = (self.a).xR(n)
        b = (self.b).xR(n)
        c = (self.c).xR(n)
        return matr3x3(a,b,c)
    def plusM(self,matr):
        a = (self.a).plusV(matr.a)
        b = (self.b).plusV(matr.b)
        c = (self.c).plusV(matr.c)
        return matr3x3(a,b,c)
    def minusM(self,matr):
        a = (self.a).minusV(matr.a)
        b = (self.b).minusV(matr.b)
        c = (self.c).minusV(matr.c)
        return matr3x3(a,b,c)
    def xV(self,vect):
        x = (self.a).dotV(vect)
        y = (self.b).dotV(vect)
        z = (self.c).dotV(vect)
        return vector(x,y,z)
    def xM(self,matr):
        a = vector((self.a).dotV(matr.column1),(self.a).dotV(matr.column2),(self.a).dotV(matr.column3))
        b = vector((self.b).dotV(matr.column1),(self.b).dotV(matr.column2),(self.b).dotV(matr.column3))
        c = vector((self.c).dotV(matr.column1),(self.c).dotV(matr.column2),(self.c).dotV(matr.column3))
        return matr3x3(a,b,c)
    def MRot(vector,angle):
        a = vector(0, vector.z, -vector.y)
        b = vector(-vector.z, 0, vector.x)
        c = vector(vector.y, -vector.x, 0)
        s = matr3x3(a, b, c)
        rotation_matrix = (matr3x3.I()).plusM(s.xR(math.sin(angle)))
        temp_matr = (s.xM(s)).xR(1 - math.cos(angle))
        return rotation_matrix.plusM(temp_matr)
