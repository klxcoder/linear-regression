"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt

def f(a: float, b: float, c: float, x: float) -> float:
    return a*x*x + b*x + c

def main():
    print(f(1, 2, 5, 2)) # 13
    x = np.arange(-20, 20)
    y = x*x + 2*x + 5
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()