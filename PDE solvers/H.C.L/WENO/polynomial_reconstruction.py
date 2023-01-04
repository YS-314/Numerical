import math
import numpy as np

#determine coefficients for WENO reconstruction scheme in a uniform grid
class rec_coeff:
    def __init__(coeff,r,s):
        coeff.r = np.array(r)
        coeff.s = np.array(s)
        coeff.len = min(coeff.r.shape,coeff.s.shape)
        coeff.coeff = np.zeros(coeff.len)
    
    def crj(j):
        return j
    


def crj_u(r,s,j):
    k = r+s+1
    X = 0
    for m in range(j+1,k+1):
        def fcrj_n1(q):
            return r - q + 1
        def fcrj_n(l):
            return prod_neq(0,k,[m,l],fcrj_n1)
        def fcrj_d(l):
            return m - l
        
        X += sum_neq(0,k,[m],fcrj_n)/prod_neq(0,k,[m],fcrj_d) #denominator correct
    return X

def crjt_u(r,s,j):
    return crj_u(r-1,s+1,j) 
