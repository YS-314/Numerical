import numpy as np


#note: ist and iend must be a list
class u_xi:
    def __init__(uio,ist, iend,delta):
        uio.ist = np.array(ist)
        uio.iend = np.array(iend)
        uio.delta = np.array(delta)

    def cfi(uio,fi):
        uio.fi = np.array(fi) 
        

    def cfi_ce(uio,fi):
        if fi.shape == tuple(uio.iend-uio.ist):
            uio.fi = np.array(fi)
        else:
            raise IndexError("fi's length does not match with object")

    def fi(uio,i)
        return uio.fi[i]

    def ui(uio, i):
        return i*uio.delta

class u_xi2:
    def __init__(ui,start,delta,i):
        ui.start = start
        ui.delta = delta
        ui.ir 


#Non uniform grid 
class nu_xi:
