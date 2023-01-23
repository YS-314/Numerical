import numpy as np
from mfun.misc.array import elwop

#note: ist and iend must be a list
class u_xi:
    def __init__(uio,ist, iend,delta, bound):
        uio.ist = np.array(ist)
        uio.iend = np.array(iend)
        uio.delta = np.array(delta)
        uio.bd = bound

    def cfi(uio,fi):
        uio.fi = np.array(fi, dtype = object) 
        

    def cfi_ce(uio,fi):
        if fi.shape == tuple(uio.iend-uio.ist):
            uio.fi = np.array(fi)
        else:
            raise IndexError("fi's length does not match with object")

    def fi(uio,i):
        if uio.ist<=i<=uio.iend:
            return uio.fi[i]
        else: 
            return 

    def ui(uio, i):
        return i*uio.delta

    def uil(uio, I):
        return np.array([uio.ui(I[x]) for x in np.ndindex(I.shape[:I.ndim-1])])


class u_xi2:
    def __init__(ui,start,delta,i):
        ui.start = start
        ui.delta = delta
        ui.ir 


#Non uniform grid 
class nu_xi:
    def __init__(grid,coord):
        grid.grid = np.array(coord, dtype = object)
        grid.dx = np.diff(mesh.mesh)
    
    def ui(grid, i):
        return grid.grid[i]



