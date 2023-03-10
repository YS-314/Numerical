import itertools
import math
import numpy as np
import sympy
from mfun.misc.misc_mfun import range1
from mfun.misc.neq_sp import prod_neq

# for 1D
def poly1c(j, rj, alpha = 1):
	'''n = len(rj)
	cj = [0]*(n+1)#np.zeros(n+1)
	for j in range1(n+1):'''
		
	cj = alpha*(-1)**(n+j)*math.fsum([math.prod(x)for x in list(itertools.combinations(rj,n-j))])
	return cj

#recursive definition
def poly1(rj, alpha = 1):
	cj = [0]*(n+1)
	def rec_cj(j,):

    return     

def pcf(coeff):
    x = sympy.Symbol('x')
    P = math.prod(x - coeff)
    C = P.expand().aspoly().all_coeffs()
    return C


def poly_el(cf, L):
    def poly_e(x):
        #cf: 2D array of coeff of degree 
        xn = x
        X = cf[0] #coefficient for x^0 (constant)
        for j in range(1,len(cf)):
            X += cf[j]*xn
            xn *= x
        return X
    return [poly_e(xn) for xn in L]

def poly_e2(cf, x):
    def polx(x1):
        X = cf[0]
        for i in range(1,len(cf)):
            X += cf[i]*(x1**i)
        return X
    return [polx(xn) for xn in x]

def poly_r(x, rj, alpha = 1): #fastest
    def polr(x1):
        X = x1 - rj[0]
        for i in range(1,len(rj)):
            X *= x1 - rj[i]
        return X
    return [alpha*polr(xn) for xn in x]

#Lagrange polynomial

#coefficients for lagrange interpolating polynomial (1D only)
def lpcf(xi, yi):
	k = min(len(xi),len(yi))-1
	cf = yi[0]*lbpcf(0,xi,k)
	



#coefficients of lagrange basis polynomial 
def lbpcf(j,xi,k):
	def alpw(m):
		return xi[j] - xi[m]
	alpha = 1/prod_neq(0,k,[j],alpw)
	xi.pop(j)
	return poly1(xi,alpha) 
	
#test
def lbpcf1(j,xi):
	def alpw(m):
		return xi[j] - xi[m]
	k = len(xi)-1
	alpha = 1/prod_neq(0,k,[j],alpw)
	xi.pop(j)
	return poly1(xi,alpha) 	

#Lagrange polynomials, barycentric form 
#-> enable addition of points
lp_bf()
