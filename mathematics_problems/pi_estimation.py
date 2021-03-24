import numpy as np


# Setting the seed for reproducibility.
SEED = 1


def sample_a_point(random_generator):
    """Sample a 2D point within a square of length 1.
    
    Returns:
        point: Dict of form {'x': x-coordinate, 'y': y-coordinate} 

    """
    # Uniform distribution is enough.
    point = dict(x=random_generator.rand(1)[0], y=random_generator.rand(1)[0])
    return point


def check_within_a_unit_circle(point):
    radius = 1.0 # Radius of a unit circle
    cartesian_distance = np.sqrt(point['x']**2 + point['y']**2)
    return cartesian_distance <= radius


def sample_and_estimate_pi(num_iterations=10000, seed=SEED):
    """Find pi by the ratio of points within a unit circle and a square tangential and enclosing it.
   
    - To enclose a unit circle, the square's length is 2*r = 2, hence the area being 4.0
    - Area of the unit circle is pi * r**2 = pi
    - Hence ratio of areas = pi / 4.0
    - pi = 4.0 * ratio of areas
    - Ratio of areas = 4.0 * (points in circle) / (points in square)
    
    """
    rng = _get_random_generator(seed)
    estimated_pi = 0 
    diff_from_prev_iteration = np.inf

    total_circle_canditates = 0

    for total_square_candidates in range(num_iterations):
        current_point = sample_a_point(random_generator=rng)
        if(check_within_a_unit_circle(current_point)):
            total_circle_canditates += 1
        
        if total_square_candidates == 0:
            new_estimated_pi = 1.0
        else:
            new_estimated_pi = 4.0 * float(total_circle_canditates) / (total_square_candidates)

        diff_from_prev_iteration = np.abs(new_estimated_pi - estimated_pi)
        estimated_pi = new_estimated_pi

    return estimated_pi 


def _get_random_generator(seed):
    return np.random.RandomState(seed=seed) 


if __name__ == "__main__":
    apple_pie = sample_and_estimate_pi(num_iterations=100000)
    print(f"Estimated pi as {apple_pie}")
    assert np.isclose(apple_pie, np.pi, rtol=1e-3)
    

