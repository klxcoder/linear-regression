"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

def f(a: float, b: float, c: float, x: float) -> float:
    return a*x*x + b*x + c

def gradient_descent(a: float, b: float, c: float) -> float:
    x: float = 0
    times: int = 1000
    alpha: float = 0.01
    small: float = 0.01
    for _ in range(times):
        dloss_dx: float = (f(a, b, c, x+small) - f(a, b, c, x))/small
        x -= alpha * dloss_dx
    return x

def main():
    x: NDArray[np.float64] = np.array(np.arange(-20, 20), dtype="float64")
    plt.plot(x, x*x + 2*x + 5)
    x_point = gradient_descent(1, 2, 5)
    plt.scatter(x_point, f(1, 2, 5, x_point), color='red')
    plt.title("f(x)=x*x + 2*x + 5")
    plt.show()

if __name__ == "__main__":
    main()