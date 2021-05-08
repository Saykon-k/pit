import copy
import cvxpy as cp
import numpy as np
import math
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()
x4 = cp.Variable()
x5 = cp.Variable()
x6 = cp.Variable()
x7 = cp.Variable()
x8 = cp.Variable()

t1 = cp.Variable()
t2 = cp.Variable()
t3 = cp.Variable()
t4 = cp.Variable()
t5 = cp.Variable()
t6 = cp.Variable()
t7 = cp.Variable()
t8 = cp.Variable()
Tk = cp.Variable()

constraints= [t4>= 20*(1-0.1*x1), t4>= 10*(1-0.15*x2),
              t5>= 20*(1-0.1*x1), t5>= 10*(1-0.15*x2), t5>= 5*(1-0.1*x3),
              t6>= 20*(1-0.1*x1), t6>= 10*(1-0.15*x2), t6>= 5*(1-0.1*x3),
              t7 >= t6 + 15*(1-0.01*x6),
              t8 >= t4 + 30*(1-0.2*x4),t8 >= t5 + 10*(1-0.2*x5),t8 >= t7 + 10*(1-0.05*x7),
              Tk>= t1 +20*(1-0.1*x1),Tk>= t2 +10*(1-0.15*x2), Tk>= t3 +5*(1-0.1*x3),
              Tk>= t4 +30*(1-0.2*x4),Tk>= t5 +10*(1-0.2*x5),Tk>= t6 +15*(1-0.01*x6),
              Tk>= t7 +10*(1-0.05*x7), Tk>= t8 +10*(1-0.1*x8),
              Tk==80,
              x1<=0,
               x2<=0,
               x3<=0,
               x4<=0,
               x5<=0,
               x6<=0,
               x7<=0,
               x8<=0]

obj = cp.Minimize(x1+x2+x3+x4+x5+x6+x7+x8)
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal val:", np.round(prob.value, 5))
k = 0
# for i in range(len(connection_from_user)):
#     print(f'x_{i}', round(float(dict_values.get(f'x_{i}').value),3))
#     k += dict_values.get(f'x_{i}').value
#     print(k)
#     print()