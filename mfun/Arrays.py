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
def minshape(arrays):
    return tuple([min(getshp_mdim(x,arrays)) for x in range(min(getdim(arrays)))])

#Get list number of dimensions in 
def getdim(arrays):
    return [np.ndim(array) for array in arrays]

#element-wise operations. Does not accept floats/integers
def elwop(func, arrays, shape = None):
    if shape == None:
        shape = arrays[0].shape
    elif shape = 0:
        #???
    result = np.zeros(shape)
    for index in np.ndindex(shape):
        result[index] = func(*tuple(arr[index] for arr in arrays))
    return result
		

