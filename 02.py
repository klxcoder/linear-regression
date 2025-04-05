"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(-20, 20)
    y = x*x + 2*x + 5
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()