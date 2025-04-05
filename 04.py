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
        """
        Calculate the result based on the given weights and inputs.

        Args:
            weights (List[float]): Change frequently, not fixed
            inputs (List[float]): Fixed, do not change

        Returns:
            List[float]: A list containing the outputs of the calculation.
        """
        pass

class F(Func):
    def calculate(self, weights: list[float], inputs: list[float]) -> list[float]:
        x, = weights
        a, b, c = inputs
        return [a*x*x + b*x + c]

def gradient_descent(f: Func, a: float, b: float, c: float) -> float:
    x: float = 0
    times: int = 1000
    alpha: float = 0.01
    small: float = 0.01
    for _ in range(times):
        dloss_dx: float = (f.calculate(weights=[x+small], inputs=[a, b, c])[0] - f.calculate(weights=[x], inputs=[a, b, c])[0])/small
        x -= alpha * dloss_dx
    return x

def main():
    x: NDArray[np.float64] = np.array(np.arange(-20, 20), dtype="float64")
    plt.plot(x, x*x + 2*x + 5)
    f = F()
    x_point = gradient_descent(f, 1, 2, 5)
    plt.scatter([x_point], f.calculate(weights=[x_point], inputs=[1, 2, 5]), color='red')
    plt.title("f(x)=x*x + 2*x + 5")
    plt.show()

if __name__ == "__main__":
    main()