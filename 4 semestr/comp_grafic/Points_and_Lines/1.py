import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)
point = Point(3.445,5.45435)
print(point)
x= 4
result = x * 10 if x < 10 else result = x / 10
print(result)