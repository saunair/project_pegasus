"""Random number generation code"""


def random_integer_list(
    lowest_number: int,
    highest_number: int, 
    numbers_required: int, 
    no_repetitions: bool = False,
    seed : int = 0,
    slope : int = 11,
    y_intercept : int = 13,
) -> list:
    """Random number generation using linear congruential generation
    
    Args:
        lowest_number: The lower-bound on the value of the random number.
        highest_number: The upper-bound on the value of the random number. 
        numbers_required: The number of random numbers to be generated.
        no_repetitions: If the values in the list cannot be repeated. 
        seed: The initial seed of the generator.
        slope: The multiplier to the piecewise linear function.
        y_intercept: The addition to the piece-wise line.

    Returns:
        List of random numbers.
    
    """

    random_numbers = []
    assert slope > 0 and slope < highest_number, "The multiplier `slope` must be positive and less than the `modulus`"
    assert y_intercept > 0 and y_intercept <= highest_number, ""
    assert seed >= 0 and seed < highest_number 
    seed %= numbers_required

    while len(random_numbers) < numbers_required: 
        seed = (seed * slope  + y_intercept) % highest_number 
        if not(no_repetitions and seed in random_numbers):
            random_numbers.append(seed + lowest_number - 1)

    return random_numbers


if __name__ == "__main__":
    print(random_integer_list(lowest_number = 0, highest_number = 20, numbers_required=15, no_repetitions=False))
