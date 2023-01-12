import itertools
import math
import numpy as np
from mfun.misc.misc_mfun import range1
from mfun.misc.neq_sp import prod_neq

# for 1D
def poly1(rj, alpha = 1):
	n = len(rj)
	cj = [0]*(n+1)#np.zeros(n+1)
	for j in range1(n+1):
		
		cj[j] = alpha*(-1)**(n+j)*math.fsum([math.prod(x)for x in list(itertools.combinations(rj,n-j))])
	return cj

def poly_e(cf, x):
	#cf: 2D array of coeff of degree 
	xn = x
	X = cf[0] #coefficient for x^0 (constant)
	for j in range(1,len(cf)):
		X += cf[j]*xn
		xn *= x
	return X

#Lagrange polynomial

#coefficients for lagrange interpolating polynomial (1D only)
def lpcf():


#coefficients of lagrange basis polynomial 
def lbpcf(j,xi):
	def alpw(m):
		return xi[j] - xi[m]
	k = len(xi)-1
	cf = np.array()
	alpha = 1/prod_neq(0,k,[j],alpw)
	return poly1(xi,alpha) #!!!!
	
	

#Lagrange polynomials, barycentric form 
lp_bf()
