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

# Example usage:
result = sum(1, 2, 3, 4, 5)
print(result)  # Output: 15.0

result_with_floats = sum(1.5, 2.5, 3.5)
print(result_with_floats)  # Output: 7.5
