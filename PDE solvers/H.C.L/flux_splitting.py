import numpy as np
import math

'''
n: (integer) index of split flux
pm: (±1) positive or negative flux
fi: (callable) f(u(xi))
'''
class 
#Roe flux
#fp: (callable) derivative of f
def roe(n,pm,fi,fp):
    if np.sign(fp(1/2*))


def roel():
    return 


#Local Lax-Friedrichs / Rusanov
#dfu: (np array)stencil of derivative of f(u) at fi
def rus(n,pm,dfu,fi):
    alpha = np.max(dfu)
    return 1/2*(fi(n)+pm*alpha)


