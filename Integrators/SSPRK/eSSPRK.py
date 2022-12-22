#explicit strong stability preserving Runge-Kutta methods (s,n) of stages s and order n
#integrates semi-discretised hyperbolic conservation laws of d/Udt = F(U)
#Uses Shu-Osher form of RK methods
import numpy as np
import math

#Shu-Osher (3,3)
class eSSP33(eSSPRK):
    alpha = tri2darr(1,3/4,1/4,1/3,0,2/3)
    beta = tri2darr(1,0,1,0,0,1)

class eSSP22(eSSPRK):
    alpha = tri2darr(1,1/2,1/2)
    beta = tri2darr(1,0,1)

class eSSP54(eSSPRK):
    alpha = tri2darr(1,0.444370493651235,0.555629506348765, ) #stopped at u^2
    beta = tri2darr(0.391752226571890,0,0,0.251891774271694) 

es_METHODS = {'eSR33': eSSP33,
           'eSR22': eSSP22,
           'eSR54': eSSP54}

def eSSP_ints1(func,t,U,method='eSR33'):
    """
    1 step of eSSP integration
    func: callable function
    t = time value (np n dimensional array) 
    U = value of U (np n dimensional array)
    method: methods (default eSR33)
    kl = keep list of evaluations
    """
    if method in es_METHODS:
        method = es_METHODS[method]
    alpha = method.alpha
    beta = method.beta
    for i in t:
        Ua


def eSSP_int(func,t0,U0,t_end,method,kl):
    for    :
        eSSP_ints1