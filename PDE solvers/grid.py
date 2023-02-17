import numpy as np
from mfun.misc.array import elwop
#grid for finite difference/finite volume methods (discrete)
#note: ist and iend must be a list
#bt is bound type, bval is boundary value
#Boundary conditions will be the first and last values of the list (-1)
#, so the range of numerically calculated values range from 1... esecond last element (-2)
#and values outside boundary conditions will be forced into a triangular domain (by rounding function) 
class u_xi:
    def __init__(uio,ist, iend,delta): #, bound, bval, bt = 0
        uio.ist = np.array(ist)
        uio.iend = np.array(iend)
        uio.delta = np.array(delta)
        '''uio.bt = bt
        


        uio.bd = bound'''

    def cfi(uio,fi):
        uio.fi = np.array(fi, dtype = object) 
        

    def cfi_ce(uio,fi):
        if fi.shape == tuple(uio.iend-uio.ist):
            uio.fi = np.array(fi)
        else:
            raise IndexError("fi's length does not match with object")
#Implement Dirichlet boundary condition for PDE
    def fi(uio,i):
        return uio.fi[i]
        # 0 and -1 (for last element) will be the boundary conditions
        '''if bt == 0:
            if uio.ist<=i<=uio.iend:
                return uio.fi[i]
            else: 
                return uio.bd
        elif bt == 1:
            if i>=uio.iend:
                return uio.fi[i]
            else: 
                return uio.bd[]'''

    def ui(uio, i):
        return i*uio.delta

    def uil(uio, I):
        return np.array([uio.ui(I[x]) for x in np.ndindex(I.shape[:I.ndim-1])])


'''class u_xi2:
    def __init__(ui,start,delta,i):
        ui.start = start
        ui.delta = delta
        ui.ir 
'''

#Non uniform grid 
class nu_xi:
    def __init__(grid,coord):
        grid.grid = np.array(coord, dtype = object)
        grid.dx = np.diff(grid.grid)
    
    def ui(grid, i):
        return grid.grid[i]



