from math import *
from gl import *

def GetZ(x, y, H):
        x0 = trunc(x)
        y0 = trunc(y)
        tempx = x - x0
        tempy = y - y0

        if (x0 + y0) % 2 == 0:
                square = "positive"
        else:
                square = "negative"

        if square == "positive":
                if tempx > tempy:
                        triangle = "top"
                        V1 = Vector3(x0,y0+1,H[x0][y0+1])
                        V12 = Vector3(1,0,H[x0+1][y0+1] - H[x0][y0+1])
                        V13 = Vector3(0,-1,H[x0][y0] - H[x0][y0+1])
                else:
                        triangle = "bot"
                        V1 = Vector3(x0+1,y0,H[x0+1][y0])
                        V12 = Vector3(0,1,H[x0+1][y0+1] - H[x0+1][y0])
                        V13 = Vector3(-1,0,H[x0][y0] - H[x0+1][y0])
        else:
                if tempy < 1 - tempx:
                        triangle = "bot"
                        V1 = Vector3(x0,y0,H[x0][y0])
                        V12 = Vector3(0,1,H[x0][y0+1] - H[x0][y0])
                        V13 = Vector3(1,0,H[x0+1][y0] - H[x0][y0])
                else:
                        triangle = "top"
                        V1 = Vector3(x0+1,y0+1,H[x0+1][y0+1])
                        V12 = Vector3(-1,0,H[x0][y0+1] - H[x0+1][y0+1])
                        V13 = Vector3(0,-1,H[x0+1][y0] - H[x0+1][y0+1])

        
        N = V12.xV(V13)
        D = -N.dotV(V1)
        z = -(N.x*x+N.y*y+D)/N.z
        
        return z


