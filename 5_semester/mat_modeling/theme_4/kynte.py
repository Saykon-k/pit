import math
import numpy as np
def fucntion(x,y):
    return x**2-2*y

def kunte(x,y):
    h = 0.1
    k1 = fucntion(x,y)

    k2 = fucntion(x+h/2,y+h*k1/2)

    k3 = fucntion(x+h/2,y+h*k2/2)

    k4 = fucntion(x+h,y+h*k3)

    y_res = y + h/6*(k1+2*k2+2*k3+k4)
    return y_res

y = 1
for i in np.arange(0.0, 1.0, 0.1):
    y = kunte(i,y)
    print(y)
