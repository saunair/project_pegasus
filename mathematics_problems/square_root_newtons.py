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
