import numpy as np


def gaussian(mu, x, sigma):
    """Return the gaussian probability of the variable `x`."""
    c = 1 / np.sqrt(2 * np.pi * (sigma ** 2))
    exponent_term = -np.sqrt(((x - mu)**2) / sigma**2)
    return c * np.exp(exponent_term)


def test_gaussian():
    # Test the gaussian probability at the mean.
    probability = gaussian(
        mu=0, x=0, sigma=1.0
    )
    assert np.isclose(
        probability, 0.3989, atol=1e-3
    ), f"estimated probability {probability} needs to be 1.0"

    # Test the gaussian probability at sigma=0.5 
    probability = gaussian(
        mu=0, x=0.5, sigma=1.0
    )
    assert np.isclose(probability, 0.2419, atol=1e-3), f"{probability} should be 0.606"

if __name__ == "__main__":
    test_gaussian()
