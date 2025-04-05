"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from abc import ABC, abstractmethod

class Func(ABC):
    @abstractmethod
    def calculate(self, weights: list[float], inputs: list[float]) -> list[float]:
        pass

class F(Func):
    def calculate(self, weights: list[float], inputs: list[float]) -> list[float]:
        a, b, c = weights
        x, = inputs
        return [a*x*x + b*x + c]

# def f(a: float, b: float, c: float, x: float) -> float:
#     return a*x*x + b*x + c

def gradient_descent(f: Func, a: float, b: float, c: float) -> float:
    x: float = 0
    times: int = 1000
    alpha: float = 0.01
    small: float = 0.01
    for _ in range(times):
        dloss_dx: float = (f.calculate([a, b, c], [x+small])[0] - f.calculate([a, b, c], [x])[0])/small
        x -= alpha * dloss_dx
    return x

def main():
    x: NDArray[np.float64] = np.array(np.arange(-20, 20), dtype="float64")
    plt.plot(x, x*x + 2*x + 5)
    f = F()
    x_point = gradient_descent(f, 1, 2, 5)
    plt.scatter([x_point], f.calculate([1, 2, 5], [x_point]), color='red')
    plt.title("f(x)=x*x + 2*x + 5")
    plt.show()

if __name__ == "__main__":
    main()