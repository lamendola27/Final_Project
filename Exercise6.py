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