"""
Check out https://www.youtube.com/watch?v=gMlf1ELvRzc ; Veritasium is a good addiction to have. 
We are using an area sampling method. Instead of doing a perimeter method like Archimedes's method of polygon ratios, 
we are just taking ratios of areas in this code. We can do that only using a computer using randomness. 
A similar method might be using integration to find out the area of the circle and the area of the square. 

- Side note, Issac Newton as a motherfucking genius. It took me 28 years to appreciate his contributions to the world. 

"""
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


def integration_method(num_of_rectangles):
    """Following the method here: https://www.youtube.com/watch?v=uK2OQMUAUDQ
    
    Basically `num_of_rectangles` is the number of rectangles representing a quarter circle.

    """
    estimated_area_of_quarter = 0.
    width = 1. / num_of_rectangles
    for rectangle_num in range(1 , num_of_rectangles):
        x_k = (rectangle_num  - 1) * width  # first x starts from 0, hence the -1
        # Applying the circle equation to find "y"
        y_k = np.sqrt(1 - x_k**2)

        # y_k is the height of the rectangle, i.e. length
        current_area = y_k * width
        estimated_area_of_quarter += current_area

    # pi * r^2 / 4 = total_area_of_of_quarter; r=1 in this case.
    pi = estimated_area_of_quarter * 4   
    return pi


if __name__ == "__main__":
    apple_pie = sample_and_estimate_pi(num_iterations=100000)
    print(f"Estimated pi using random area sampling as {apple_pie}")
    assert np.isclose(apple_pie, np.pi, rtol=1e-3)
    
    pecan_pie = integration_method(10000)
    print(f"Estimated pi using summation as {pecan_pie}")
    assert np.isclose(pecan_pie, np.pi, rtol=1e-3)

