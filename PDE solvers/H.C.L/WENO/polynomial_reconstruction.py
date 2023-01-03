import math
import numpy

#determine coefficients for WENO reconstruction scheme in a uniform grid
def crj_u(r,s,j):
    k = r+s+1
    for m in range(j+1,k+1):
        def fcrj_d(l):
            return m - l
        /prod_neq(0,k,[m],)


