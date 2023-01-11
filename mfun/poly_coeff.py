import itertools
import math
import numpy as np
from mfun.misc.misc_mfun import range1

def poly1(rj, alpha = 1):
	n = len(rj)
	cj = [0]*(n+1)#np.zeros(n+1)
	for j in range1(n+1):
		
		cj[j] = alpha*(-1)**(n+j)*math.fsum([math.prod(x)for x in list(itertools.combinations(rj,n-j))]) #list(itertools.combinations(rj,n-j))#math.fsum(
		'''cj[j]=alpha*(-1)**(n+j)*math.fsum(itertools.combinations(rj,n-j))'''
	return cj

#coefficients for lagrange interpolating polynomial
def lpcoeff()


