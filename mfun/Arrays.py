#Support for array and tensors
import itertools

#element-wise operations
def elwop(f,*array):
	n = min(*array.shape)
	return [f(x) x in itertools.product(*array)]
		

