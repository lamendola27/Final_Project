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
plt.show()

### Exercise 2
import matplotlib.pyplot as plt
import numpy as np
P=np.linspace(0,4,10000)
m = 1
X = []
Y = []
for u in P:
    X.append(u)
    m = np.random.random()
    for n in range(500):
      m=(u*m)*(1-m)
    Y.append(m)
plt.plot(X, Y, ls='', marker=',')
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

### Exercise 6
import numpy as np
import matplotlib.pyplot as plt 

x0=0
x=x0
if x < 1/2:
    g_x = x
else:
    g_x = (1 - x)
a =0.5 # start interval
b = 2.5 # end interval
n = 0.1 # size of intervals
x0 = 0
xmax = 5
ymax = 5
x = x0
ynext = g_x
X = []
Y = []
for i in range(0,3,1):
    xnew = ynext
    xold = x 
    x = xnew
    ynext = g_x
    X.append(xold)
    X.append(x) 
    X.append(x)
    Y.append(xnew) 
    Y.append(xnew) 
    Y.append(ynext)
q = 200
k = np.linspace(0, xmax, q+1)
y = f(t)
def f(t):
    k = np.linspace(0, xmax, q+1)
    for t in k:
        y = f(t)
    i = np.linspace(0, xmax, q+1)
    return y,i,k
plt.figure()
plt.plot(X, Y, label='cobweb')
plt.plot(i, i, label='y=x')
plt.plot(k, y, label='f(x)')
plt.ylim([0, ymax])
plt.legend()
plt.show()

