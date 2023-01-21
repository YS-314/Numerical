#Support for array and tensors
#requires all lists to be numpy arrays, while multiple lists are to be stored in tuples
import itertools

#package arrays
#returns tuple containing numpy arrays
def packarr(*arrays):
	return arrays

#shape of arrays at mth dimension
def getshp_mdim(m, arrays):
    return tuple(arr.shape[m] for arr in arrays)

#
def minshape(*arrays):
    return tuple([min(getshp_mdim(x,arrays)) for x in range(min(getdim(arrays)))])

#Get list number of dimensions in 
def getdim(arrays):
    return [np.ndim(array) for array in arrays]

#element-wise operations
def elwop(f,*array):
	n = min(*array.shape)
	return n #[f(x) x in itertools.product(*array)]
		

