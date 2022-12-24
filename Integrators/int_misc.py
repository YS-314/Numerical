import numpy as np

def tri2darr(*coeff):
  n = int(1/2*((8*len(coeff)+1)**(1/2)-1))
  j = 0
  X = np.zeros((n,n))
  cl = 0
  while j < n:
    for x in range(0,j+1):
      X[j,x] = coeff[cl+x]
    j += 1
    cl += j
  return X
