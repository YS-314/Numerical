#Support for array and tensors
#requires all lists to be numpy arrays
import itertools

#package arrays
#returns tuple containing numpy arrays
def packarr(*arrays):
	return arrays

#shape of arrays at mth dimension
def getshp_mdim(m, arrays):
    return tuple(arr.shape[m] for arr in arrays)

#Get list number of dimensions in 
def getdim(arrays):
    return [np.ndim(array) for array in arrays]

#element-wise operations
def elwop(f,*array):
	n = min(*array.shape)
	return n #[f(x) x in itertools.product(*array)]
		

