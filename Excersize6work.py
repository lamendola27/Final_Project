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

###################################################

import numpy as np
import matplotlib.pyplot as plt 

x0=0
x=x0

def tent_map(x, n=3):
    outputs = np.array([])
    for i in range(0, n):
        inputs = np.append(inputs, x)
        if x < 0.5:
            x = x
        elif x > 0.5:
            x = 1-x
        outputs = np.append(outputs, x)
    return outputs



xmax = 50
ymax = 50
ynext = g(x)
X = []
Y = outputs 
Lin = np.linspace(5,25)
for i in Lin:
    xnew = ynext
    xold = x 
    x = xnew
    ynext = g(x)
    X.append(xold)
    X.append(x) 
    X.append(x)
    Y.append(xnew) 
    Y.append(xnew) 
    Y.append(ynext)
plt.figure()
plt.plot(X, Y, label='cobweb')
plt.ylim([0, ymax])
plt.legend()
plt.show()

#############################################

import numpy as np
import matplotlib.pyplot as plt 
    #plt.plot(diagnolline)
def cobweb(f, x0, n, xmax, ymax):
    x = x0
    ynext = f(x)
    X = []
    Y = []
    for i in range(0.5, n, 0.1):
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

import numpy as np
import matplotlib.pyplot as plt 


for x in np.linspace(0.5, 2.5, 21):
    def g(x, p=1):
        if x < 1/2:
            y = p*x
        else:
            y = p*(1 - x)
        return y

plt.figure()
plt.plot(x, y)



print(cobweb(f=g, x0=0, n=2.5,xmax= 5, ymax=5))


#####################################################

import numpy as np
import matplotlib.pyplot as plt 

def cobweb(f, x0=1, n=2.5, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5):
    x = x0
    ynext = f(x)
    X = []
    Y = []
    for k in range(0, 200, 2):
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
    
    t = np.arange(0, 2.5, 0.1)

    y = []
    for i in range(len(t)):
        y.append(g(t[i]))

    i = np.linspace(0, 2.5)

    plt.figure()
    plt.plot(X, Y, label='cobweb')
    plt.plot(t, y, label='tent map') # tent map
    plt.plot(i, i, label='y=x') # diaganol line
    plt.legend()
    plt.show()

def g(x, p=1):
    if x < 1/2:
        return p*x
    else:
        return p*(1-x)

#print(cobweb(f=g, x0=1, n=2.5, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5))

#####################################################################


import numpy as np
import matplotlib.pyplot as plt 

def cobweb(f, x0=2, n=200, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5):
    x = x0
    ynext = f(x)
    X = []
    Y = []
    for k in range(0, 200, 2):
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
    
    t = np.arange(0, 2.5, 0.1)

    y = []
    for i in range(len(t)):
        y.append(g(t[i]))

    i = np.linspace(0, 2.5)

    plt.figure()
    plt.plot(X, Y, label='cobweb')
    plt.plot(t, y, label='tent map') # tent map
    plt.plot(i, i, label='y=x') # diaganol line
    plt.legend()
    plt.show()

print(cobweb(f=g, x0=2, n=200, xmin=0, xmax=2.5, ymin=0, ymax=2.5))












