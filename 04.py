"""
Use gradient descent to find the minimum of the function f(x)=x*x + 2*x + 5
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from abc import ABC, abstractmethod

class Func(ABC):
    def __init__(self, inputs: list[float]):
        self.inputs: list[float] = inputs
    @abstractmethod
    def calculate(self, weights: list[float]) -> list[float]:
        pass

class F(Func):
    def calculate(self, weights: list[float]) -> list[float]:
        x, = weights
        a, b, c = self.inputs
        return [a*x*x + b*x + c]

def gradient_descent(f: Func) -> float:
    x: float = 0
    times: int = 1000
    alpha: float = 0.01
    small: float = 0.01
    for _ in range(times):
        dloss_dx: float = (f.calculate([x+small])[0] - f.calculate([x])[0])/small
        x -= alpha * dloss_dx
    return x

def main():
    x: NDArray[np.float64] = np.array(np.arange(-20, 20), dtype="float64")
    plt.plot(x, x*x + 2*x + 5)
    f = F(inputs=[1, 2, 5])
    x_point: float = gradient_descent(f)
    plt.scatter([x_point], f.calculate([x_point]), color='red')
    plt.title("f(x)=x*x + 2*x + 5")
    plt.show()

if __name__ == "__main__":
    main()