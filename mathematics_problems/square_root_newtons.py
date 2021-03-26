"""
Here: f(x) = x^2 - A 
We've got to minimize f(x) to find the square root of A, which is x. 

Newton-Raphson's method - 

Primer: 
    For a curve, tangent at point x_k is:
        a) y = f'(x)*(x - x_k) + f(x_k)  (slope is f'(x), f(x_k) is "c")

The method now says, let's start from an initial condition: x_k
The next best estimate of the root: x_k+1 is the x-intercept of tangent at x_k; which means y=0. 
Plugging this at a), 
    0 = f'(x_k)*(x_k+1 - x_k) + f(x_k)
    x_k+1 = x_k - f(x_k) / f'(x_k) 

Now x_k+1 = x_k for the next iteration. 

side note: it is mesmerizing to see how newton thought algorithmically. Math is pretty much algorithms with constraints. 
This also made me read about quasi-newton methods, like BFGS, which I had used in camera calibration. The appreciation for mathematics isn't enough. 

"""


import numpy as np


def square_root(number, accuracy_tolerance=1e-4, num_iterations=1000):
    """Estimate the square root of a natural `number`.
    
    Args:
        number: 
        accuracy_tolerance: 
        num_iterations: 

    Returns:
        the estimated square root
    
    Raises:
        ValueError: If number isn't a natural number.
    
    """
    if number < 0:
        raise ValueError("Cannot estimate the square root of a negative number.")

    estimated_root = number

    for _ in range(num_iterations):
        new_estimated_root = 0.5 * (estimated_root + (float(number) / estimated_root))
        if np.abs(new_estimated_root - estimated_root) < accuracy_tolerance:
            break
        estimated_root = new_estimated_root

    return estimated_root


if __name__ == "__main__":
    print(f"Square root for 3 is: {square_root(3)}")
    print(f"Square root for 100 is: {square_root(100)}")
    print(f"Square root for 17 is: {square_root(17)}")
    print(f"Square root for -1 is: {square_root(-1)}")
