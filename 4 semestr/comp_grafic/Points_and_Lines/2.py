class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distanceTo(self,point):
        print(point.y)
        return (((self.x-point.x)**2+(self.y-point.y)**2)**0.5)
p = Point(1,0)
point = Point(0,1)
print(p.distanceTo(point))