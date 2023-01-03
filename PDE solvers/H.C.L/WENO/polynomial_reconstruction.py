import math
import numpy

#determine coefficients for WENO reconstruction scheme in a uniform grid
def crj_u(r,s,j):
    k = r+s+1
    X = 0
    for m in range(j+1,k+1):
        def fcrj_n1(q):
            return r - q + 1
        def fcrj_n(l):
            return prod_neq(0,k,np.sort([m,l]),fcrj_n1)
        def fcrj_d(l):
            return m - l
        
        X += sum_neq(0,k,[m],fcrj_n)/prod_neq(0,k,[m],fcrj_d) #denominator correct
    return X


