
#miscellaneous math functions
import numpy as np

def range1(stop, start=0, step=1):
    if start == stop:
        return np.array([start])
    else: return range(start, stop, step)

