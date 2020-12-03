# Final Project Exercises
# Lindsay Amendola
# Carli Peters
# 22 December 2020

# Exercise 1
import numpy as np 
import matplotlib as plt
def tentmap(y, n):
 # need to create lists for input and output
 inp = np.array([])
 out = np.array([])
 for i inp range(1, n):
 	inp = np.append(inp, y)
 	if y < 0.5:
 		y = 2*y
 	elif y >= 0.5:
 		y = 2 - 2 * y
 	out = np.append(out, y)
 print(inp)
 print(out)
 tentmap(0.34685264,3)


#Exercise 5 Very rough draft 
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
		X.append(xold)
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