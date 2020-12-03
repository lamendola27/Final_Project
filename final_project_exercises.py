# Final Project Exercises
# Lindsay Amendola
# Carli Peters
# 22 December 2020

# Exercise 1
import numpy as np 
import matplotlib as plt
def tentmap(y, n):
 # need to create lists for input and output
	a = 2 
	inp = np.array([])
	out = np.array([])
	for i in range(1, n):
		inp = np.append(inp, y)
		if y < 0.5:
			y = a*y
		elif y >= 0.5:
			y = a - a * y
		out = np.append(out, y)
	return inp, out 
print(tentmap(0.34685264,3))


#Exersice 1 attempt that returns a grapgh of the funtion
import matplotlib.pyplot as plt
%matplotlib inline
a = 2
def f(n):
	if n < 1/2:
		f_x = a*n
	else:
		f_x = a*(1-n)
	return f_x
n = 0
y = [n]
x = range(0,15)
for i in x[1:]:
	n = f(n)
	y.append(n)
plt.scatter(x,y)
plt.plot(x,y)




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
	
	x1 = np.linspace(0, 1, 200)
	y1 = np.cos(x1)
	plt.plot(x1, y1)

	diagnolline = []
	for i in range(0,2):
		diagnolline.append(i)

	plt.plot(diagnolline)
	plt.legend()
	plt.show()

def f(x):
    return np.cos(x)

print(cobweb(f, 1.0, 200, 0, 1.5, 0, 1))

