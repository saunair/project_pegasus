import numpy as np


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __repr__(self):
        return f"""x: {self.__x}, y: {self.__y}"""

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x


def bisection_search(
    math_function, endpoint_min, 
    endpoint_max, tolerance=1e-4, max_iteration=1000
):
    """We expect `math_function` to have its minima between `endpoint_min` and `endpoint_max`.

    Parameters
    ----------
    math_function: a function that takes in a float value with signature math_function(x)
    endpoint_min: float
    endpoint_max: float

    Returns
    -------
    Point: Point at the minima

    Raises
    ------
    AssertionError: If endpoint_min > endpoint_max
    AssertionError: If sign(math_function(endpoint_min)) == sign(math_function(endpoint_max))

    """
    assert endpoint_min < endpoint_max, "Input range not ordered."
    assert np.sign(math_function(endpoint_min)) != np.sign(math_function(endpoint_max))
    lower_x = endpoint_min
    higher_x = endpoint_max

    previous_val_at_x = np.inf
    current_iteration = 0
    while current_iteration < max_iteration:
        current_x = (higher_x + lower_x) / 2.0
        current_y_at_x = math_function(current_x)

        if (
            np.isclose(current_y_at_x, previous_val_at_x, atol=tolerance) or 
            np.isclose(current_y_at_x, 0, atol=tolerance) or 
            np.isclose(current_x / 2, higher_x, tolerance))
        :
            break

        # If the sign at the lower point and the mid point are the same, 
        # we make the lower bound go to the mid-point. 
        if np.sign(current_y_at_x) == np.sign(function(lower_x)):
            lower_x = current_x
        else: 
            # If not, we have crossed the zero, hence retain the lower point and update the higher.
            higher_x = current_x
        current_iteration += 1

    return Point(current_x, current_y_at_x)


if __name__ == "__main__":
    function = lambda x: 2 * x + 3
    assert np.isclose((bisection_search(math_function=function, endpoint_min=-20, endpoint_max=20)).x, -1.5, atol=1e-3)

    function = lambda x: x**2 - 4
