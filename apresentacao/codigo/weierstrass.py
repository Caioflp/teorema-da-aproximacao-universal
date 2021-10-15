import scipy.special
from matplotlib import pyplot as plt
import numpy as np

def bernstein(n, x, g):
    y = 0
    for k in range(n+1):
        y += g(np.divide(k, n))*scipy.special.comb(n, k, exact=True)*np.power(x, k)*np.power(1-x, n-k)
    return y

X = np.linspace(1, 2, 100)
f = np.log
Y_true = f(X)
Y_approx = [bernstein(20, x, f) for x in X]

plt.plot(X, Y_true)
plt.plot(X, Y_approx)
plt.show()
