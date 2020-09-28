from __future__ import print_function

import sys
import numpy as np
import time

from datetime import datetime


if __name__ == "__main__":


	x = np.ones(200000000)*2
	y = np.ones(200000000)*2




	start = time.time()
	result1 =0

	result1=np.sum(x*y)


	done = time.time()
	print (result1)
	elapsed = done - start
	print('Numpy Elapsed Time: ', elapsed)



# Now, let us do the same thing and compare the time.

	startNew = time.time()
	result2 =0

	for i in range (20000000):
		result2 = result2 + x[i]*y[i]



	doneNew = time.time()
	print (result2)
	elapsedNew = doneNew - startNew
	print('ForLoop Elapsed Time: ',  elapsedNew)
