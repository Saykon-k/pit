class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        for_pr_A = "-%.2f" % (abs(self.A)) if self.A < 0 else "%.2f" % (self.A)
        for_pr_B = "- %.2f" % (abs(self.B)) if self.B < 0 else "+ %.2f" % (self.B)
        for_pr_C = "- %.2f" % (abs(self.C)) if self.C < 0 else "+ %.2f" % (self.C)
        return "{}x {}y {} = 0".format(for_pr_A, for_pr_B, for_pr_C)

    def fromCoord(x1, y1, x2, y2):
        return Line(y1 - y2, x2 - x1, x1 * y2 - x2 * y1)

    def distanceToZero(self):
        if (self.A ** 2 + self.B ** 2) ** 0.5 != 0:
            return abs(self.C) / (self.A ** 2 + self.B ** 2) ** 0.5
        else:
            return self.C
    def distanceToPoint(self, point):
        if (self.A**2+self.B**2)**0.5 != 0:
            return abs(self.A*point.X + self.B*point.Y + self.C)/(self.A**2+self.B**2)**0.5
    def isParallel(self, line):
        return abs(self.A*line.B - self.B*line.A) <= 0.001
    def intersection(self, line):
        if not self.isParallel(line):
            x_point = (line.C*self.B - self.C*line.B)/(line.B*self.A - self.B*line.A)
            y_point = (line.C*self.A - self.C*line.A)/(-line.B*self.A + self.B*line.A)
            return Point(x_point,y_point)
        else:
            return None
    def  oneSide(self,point1,point2):
        first = self.A*point1.X + self.B*point1.Y + self.C
        sec  =self.A*point2.X + self.B*point2.Y + self.C
        return False if first*sec <0 else True

    def normalize(self):
        if self.C != 0:
            self.A = self.A / self.C
            self.B = self.B / self.C
            self.C = 1
        elif self.A != 0:
            self.C = 0
            self.B = self.B / self.A
            self.A = 1
        else:
            self.A = 0
            self.B = 1
            self.C = 0

    def perpendicularLine(self, point):
        a = -1
        if self.B != 0:
            b = self.A/self.B
        else:
            b = self.A
        c = point.X - b*point.Y
        return Line(-a, -b, -c)

    def parallelLine(self,point):
        c = - self.A * point.X - self.B * point.Y
        return Line(self.A, self.B, c)

    def projectionLength(self,point,point1):
        per1 = self.perpendicularLine(point)
        per2 = self.perpendicularLine(point1)
        p1_fin = self.intersection(per1)
        p2_fin = self.intersection(per2)
        return ((p1_fin.X-p2_fin.X)**2+(p1_fin.Y-p2_fin.Y)**2)**0.5

    def middlePoint(self, point):
        p = self.intersection(self.perpendicularLine(point))
        return Point((point.X + p.X) / 2, (point.Y + p.Y) / 2)

    def symmetricPoint(self,point):
        p = self.intersection(self.perpendicularLine(point))
        return Point((p.X*2-point.X),(p.Y*2-point.Y))

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __str__(self):
        return "(%.2f, %.2f)" % (self.X, self.Y)

    def distanceTo(self, point):
        return ((self.X - point.X) ** 2 + (self.Y - point.Y) ** 2)**0.5

l = Line(1,0,3)
pont = Point(0,1)
pont1 = Point(1,0)

print(l.symmetricPoint(pont))