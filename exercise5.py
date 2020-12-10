import numpy as np
import matplotlib.pyplot as plt 
    #plt.plot(diagnolline)
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
		X.append(xold)
		X.append(x) 
		X.append(x)
		Y.append(xnew) 
		Y.append(xnew) 
		Y.append(ynext)

	k = np.linspace(0, xmax, n+1)
	y = f(k)
	i = np.linspace(0, xmax, n+1)
	plt.figure()
	plt.plot(X, Y, label='cobweb')
	plt.plot(i, i, label='y=x')
	plt.plot(k, y, label='f(x)')
	plt.ylim([0, ymax])
	plt.legend()
	plt.show()

print(cobweb(np.cos, 1.0, 200, 0, 1.5, 0, 1))














