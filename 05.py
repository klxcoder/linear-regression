"""
Use gradient descent to find the minimum of the function f(x)
"""

import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from typing import Any

class Func(ABC):
    def __init__(self, inputs: list[float]):
        self.inputs: list[float] = inputs
    @abstractmethod
    def calculate(self, weights: list[float]) -> list[float]:
        pass
    def get_output(self, weights_arr: list[list[float]]) -> list[list[float]]:
        return list(map(lambda weights:self.calculate(weights), weights_arr))

class F1(Func):
    def calculate(self, weights: list[float]) -> list[float]:
        x, = weights
        a, b, c = self.inputs
        return [a*x*x + b*x + c]

class F2(Func):
    def calculate(self, weights: list[float]) -> list[float]:
        x, = weights
        a, b = self.inputs
        return [abs(x+a) + b]

def gradient_descent(f: Func) -> float:
    x: float = 0
    times: int = 1000
    alpha: float = 0.01
    small: float = 0.01
    for _ in range(times):
        dloss_dx: float = (f.calculate([x+small])[0] - f.calculate([x])[0])/small
        x -= alpha * dloss_dx
    return x

def draw(ax: Any, f: Func, title: str, x: list[list[float]]):
    ax.plot(x, f.get_output(x))
    x_point: float = gradient_descent(f)
    ax.scatter([x_point], f.calculate([x_point]), color='red')
    ax.set_title(title)

def main():
    x: list[list[float]] = list(map(lambda x: [x], list(range(-20, 20))))

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    f1 = F1(inputs=[1, 2, 5])
    draw(axes[0], f1, "f(x) = 1*x*x + 2*x + 5", x)
    
    f2 = F2(inputs=[10, 4])
    draw(axes[1], f2, "f(x) = |x + 10| + 4", x)

    plt.show()

if __name__ == "__main__":
    main()