import numpy as np

def tri2darr(*coeff):
  n = int(1/2*((8*len(coeff)+1)**(1/2)-1))
  j = int(1)
  X = np.zeros((n,n))
  cl = int(0)
  #while j < n:
    cl2 = cl + j
    #0.5*j*(j+1)
    vec = np.concatenate(coeff[cl:cl2],np.zeros(n-cl))
    #np.full((n-cl),0)?
    cl = cl2
    X = np.vstack(X,vec)
