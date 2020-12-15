import numpy as np
import matplotlib.pyplot as plt 

def cobweb(f, x0, n, xmin, xmax, ymin, ymax):
	x = x0
	ynext = f(x)
	X = []
	Y = []
	for i in range(0, n, 2):
		xnew = ynext
		xold = x 
		x = xnew
		ynext = f(x)
		X.append(xold, x, x)
		X.append(x) 
		X.append(x)
		Y.append(xnew) 
		Y.append(xnew) 
		Y.append(ynext)
	plt.figure()
	plt.plot(X, Y)
	plt.plot(x, f(x))

	diagnolline = []
	for i in range(0,100):
		diagnolline.append(i)

	plt.plot(diagnolline)
	plt.legend()
	plt.show()

print(cobweb(np.cos, 1.0, 200, 0, 1.5, 0, 1))


### exercise 6 
	plt.plot(x, f(x))
