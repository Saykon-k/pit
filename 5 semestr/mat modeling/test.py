import sympy as sym
import numpy as np
def production_cob_and_duglas():
    alfa, beta, A, K, L = sym.symbols('alfa beta A K L')
    exp = (sym.log(A*K**(alfa)*L**(beta)))
    #print(sym.diff(exp,beta))
    return  exp
def ssd(function, res):
    alfa, beta, A, K, L = sym.symbols('alfa beta A K L')
    print(sym.diff((function-res)**2,beta))
    print(sym.diff((function-res)**2,alfa))
    print(sym.diff((function-res)**2,A))
print(np.log(3)+np.log(5))
print(np.log(3*5    ))
