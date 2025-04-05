from typing import Union

def sum(*args: Union[int, float]) -> float:
    """
    This function takes an arbitrary number of numerical arguments and returns their sum.

    Parameters:
    *args: Any number of numerical arguments (int or float).

    Returns:
    float: The sum of the arguments.
    """
    total: float = 0.
    for arg in args:
        total += arg
    return total

def sum2(a: int, b: int) -> float:
    return sum(a, b)

def sum3(a: int, b: int, c: int) -> float:
    return sum(a, b, c)

s2 = sum2(1, 2)
print(s2) # 3.0

s3 = sum3(1, 2, 3)
print(s3) # 6.0