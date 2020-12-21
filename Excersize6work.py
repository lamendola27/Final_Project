
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

    t = np.arange(0, 1, 0.1)

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

def g(t, a=2):
    if t < 1/2:
        return a*t
    else:
        return a*(1-t)

print(cobweb(f=g, x0=0.1, n=200, xmin=0.5, xmax=2.5, ymin=0, ymax=2.5))










