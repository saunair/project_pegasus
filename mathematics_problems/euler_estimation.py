"""Euler's constant "e"'s estimation."""


def estimate_euler_constant(number_of_elements=1000):
    """Compound interest method where "t" tends to zero."""
    compound_growth_element = (1. + 1. / number_of_elements)
    euler_constant = 1.
    for _ in range(number_of_elements):
        euler_constant *= compound_growth_element
    return euler_constant



def estimate_euler_constant_factorial(number_of_elements=1000):
    """Estimation of euler's constant using its taylor series."""
    euler_constant = 1
    factorial = 1.
    for number in range(1, number_of_elements):
        factorial *= number
        euler_constant += 1. / factorial
    return euler_constant


if __name__ == "__main__":
    print(estimate_euler_constant(100000))
    print(estimate_euler_constant_factorial(100000))

