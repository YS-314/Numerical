import math
import numpy as np
from mfun.misc.neq_sp import sum_neq, prod_neq

#determine coefficients for WENO reconstruction scheme in a uniform grid
import itertools
class rec_coeff:
    def __init__(coeff,r,s,unif):
        coeff.r = np.array(r)
        coeff.s = np.array(s)
        coeff.shape = np.array(min(coeff.r.shape,coeff.s.shape)+(np.amax(coeff.r+coeff.s)+1,))
        coeff.coeff = np.zeros(coeff.shape)
        coeff.dim = len(coeff.shape) # do we need this?
        '''lrange = [0]*(coeff.dim)
        for d in range(coeff.dim):
            lrange[d] = range(0,coeff.shape[d])''' #should be represented more concisely with list comprehension
        lrange = [range(d) for d in coeff.shape]
        if unif == True:
            for i in itertools.product(*lrange): #unpack lrange and use for loop (x no. dimensions) to fill up n-d array
                coeff.coeff[i] = crj_u(coeff.r[i[:coeff.dim-1]],coeff.s[i[:coeff.dim-1]],i[coeff.dim-1])
    def crj_n(coeff,n):
        return coeff.coeff[n]
    def crj(coeff,j):
        return j
    


def crj_u(r,s,j):
    k = r+s+1
    X = 0
    if j<k:
        for m in range(j+1,k+1):
            X += sum_neq(0,k,[m],lambda l: prod_neq(0,k,[m,l],lambda q: r - q + 1))/prod_neq(0,k,[m],lambda l: m - l )
    return X

def crjt_u(r,s,j):
    return crj_u(r-1,s+1,j) 
