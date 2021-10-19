import scipy.special
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def bernstein(n, x, g):
    y = 0
    for k in range(n+1):
        y += g(np.divide(k, n))*scipy.special.comb(n, k, exact=True)*np.power(x, k)*np.power(1-x, n-k)
    return y

X = np.linspace(0, 1, 200)

for f, name in [( lambda x: np.sin(1/(3*(x+0.05))), "seno" ),
                ( lambda x: 1/(100*(x - .5)**2 + 1), "cauchy" ),
                ( lambda x: np.abs(np.floor(3*np.sin(x))), "cobrinha" )]:
    Y_true = f(X)
    plt.close("all")
    plt.plot(X, Y_true, label="f(x)", color="red")
    for n, color in [(5, 'skyblue'), (25, 'deepskyblue'),
                     (50, 'dodgerblue'), (100, 'mediumblue'), (500, 'blue')]:
        Y_approx = [bernstein(n, x, f) for x in X]
        plt.plot(X, Y_approx, label=f"n={n}", color=color)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc="best")
    plt.savefig(f"../figuras/weierstrass_{name}.png")
    plt.show()
