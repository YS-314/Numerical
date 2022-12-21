#explicit strong stability preserving Runge-Kutta methods (s,n) of stages s and order n
#integrates semi-discretised hyperbolic conservation laws of d/Udt = F(U)
import numpy as np
import math

#Shu-Osher (3,3)
def eSSP33(ab):
    if ab == 1:
        x = tri2darr()
