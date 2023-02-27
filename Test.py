import numpy as np
from mfun.arrays import elwop
print(elwop(lambda x, y: x+y, (np.array([1,2,3]), np.array([4,5,6]))))

import PDE_solvers.grid
testgrid = u_xi()