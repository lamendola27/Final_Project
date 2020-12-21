# Final Project Exercises
## Lindsay Amendola
## Carli Peters
## 22 December 2020

### Exercise 1
import numpy as np 
import matplotlib as plt
def tentmap(y, n):
 # need to create lists for input and output
 inp = np.array([])
 out = np.array([])
 for i in range(1, n):
 	inp = np.append(inp, y)
 	if y < 0.5:
 		y = 2*y
 	elif y >= 0.5:
 		y = 2 - 2 * y
 	out = np.append(out, y)
 print(inp)
 print(out)
tentmap(0.34685264,3)

### Exercise 4
import matplotlib.pyplot as plt
import numpy as np
P=np.linspace(1,4,500)
m= 1
X = []
Y = []
for u in P:
    X.append(u)
    m = np.random.random()
    for n in range(500):
      m=(u*m)*(1-m)
    Y.append(m)
plt.plot(X, Y, ls='', marker=',')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

### Exercise 2
import matplotlib.pyplot as plt
import numpy as np
P=np.linspace(0,4,5000)
m= 1
X = []
Y = []
for u in P:
    X.append(u)
    m = np.random.random()
    for n in range(500):
      m=(u*m)*(1-m)
    Y.append(m)
plt.plot(X, Y, ls='', marker=',')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

### Exercise 5
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

	k = np.linspace(xmin, xmax, n+1)
	y = f(k)
	i = np.linspace(xmin, xmax, n+1)
	plt.figure()
	plt.plot(X, Y, label='cobweb')
	plt.plot(i, i, label='y=x')
	plt.plot(k, y, label='cos(x)')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.ylim([ymin, ymax])
	plt.legend()
	plt.show()
    plt.savefig(fname='ex5', dpi=70)

print(cobweb(np.cos, 1.0, 200, 0, 1.5, 0, 1))

### Exercise 6
import numpy as np
import matplotlib.pyplot as plt 

def cobweb(f, x0=0.1, n=200, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5):
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

    t = np.arange(0, 1.1, 0.1)

    y = []
    for i in range(len(t)):
        y.append(g(t[i]))

    diagonal = range(0, 2)

    plt.figure()
    plt.plot(X, Y, label='cobweb')
    plt.plot(t, y, label='tent map') # tent map
    plt.plot(diagonal, diagonal, label='y=x') # diaganol line
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    plt.savefig(fname='ex6', dpi=70)

def g(t, a=2):
    if t < 1/2:
        return a*t
    else:
        return a*(1-t)

print(cobweb(f=g, x0=0.1, n=200, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5))