#Support for array and tensors
import itertools

#get shape of array
def getshp(m,*arrays):
  return tuple(arr.shape[m] for arr in np.array(arrays,dtype=object))

#element-wise operations
def elwop(f,*array):
	n = min(*array.shape)
	return n #[f(x) x in itertools.product(*array)]
		

