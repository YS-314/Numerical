import math
import numpy as np
from mfun.misc.misc_mfun import range1
from mfun.misc.neq_sp import prod_neq

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
lp_bf()
