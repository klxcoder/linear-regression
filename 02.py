"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt

def f(a: float, b: float, c: float, x: float) -> float:
    return a*x*x + b*x + c

def gradient_descent() -> tuple[float, float, float]:
    a, b, c = 0, 0, 0
    times: int = 1000
    alpha: float = 0.01
    for _ in range(times):
        dloss_da: float = 1
        dloss_db: float = 1
        dloss_dc: float = 1
        a -= alpha * dloss_da
        b -= alpha * dloss_db
        c -= alpha * dloss_dc
    return a, b, c

def main():
    x = np.arange(-20, 20)
    plt.plot(x, x*x + 2*x + 5)
    a, b, c = gradient_descent()
    plt.plot(x, a*x*x + b*x + c)
    plt.show()

if __name__ == "__main__":
    main()