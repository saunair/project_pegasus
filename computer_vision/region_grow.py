from copy import copy

import numpy as np


def spread_fire_for_location(
    fire_grid: np.ndarray, 
    elevation_grid: np.ndarray, 
    location_x: int, 
    location_y: int, 
    differential: float, 
    is_child: bool=False
) -> np.ndarray:
    """For a specific pixel and time-stamp, find all the locations where the fire can spread
    
    Args:
        fire_grid: The current locations of the fire.
        elevation_grid: The elevations of the area.
        location_x: The x coordinate of the pixel under scrutiny.
        location_y: The y coordinate of the pixel under scrutiny.
        differential: The expected differnce from the current pixel and the child pixel fulfil the ignition criteria
        is_child: If the current pixel under scrutiny is a child node. I.e it was set on fire this current time-stamp.

    Returns:
        The updated fire grid.

    """
    assert fire_grid[location_x][location_y], "Fire cannot spread from a location that hasn't been lit yet."
    
    if is_child is False:
        assert differential == 2, "Just keeping a sanity check as per the problem requirement. Diff {differntial}"

    x_len, y_len = fire_grid.shape
    if location_x == x_len - 1 or location_y == y_len - 1 or location_x < 0 or location_y < 0:
        return fire_grid
    
    # Check for all neighboring 8 locations
    for current_x in range(location_x - 1, location_x + 2):
        for current_y in range(location_y - 1, location_y + 2):
            # Skip the current location.
            if current_x == location_x and current_y == location_y:
                continue
            # If already lit, we don't have to set it or explore it.
            if fire_grid[current_x][current_y]:
                continue
            

            # Compute the elevation difference with the original location.
            elevation_diff = elevation_grid[location_x][location_y] - elevation_grid[current_x][current_y]

            # If the location is the root location, we can take the absolute to find the differential.
            fire_grid[current_x][current_y] = elevation_diff == differential if is_child else (
                np.abs(elevation_diff) <= np.abs(differential)
            )
            if current_x == 5 and current_y == 5:
                print(elevation_diff, differential, elevation_grid[location_x][location_y], elevation_grid[current_x][current_y])
            # Now spread fire for the child location with the expected monotonic increment/decrement.
            if fire_grid[current_x][current_y]:
                spread_fire_for_location(
                    fire_grid=fire_grid, 
                    elevation_grid=elevation_grid, 
                    location_x=current_x, 
                    location_y=current_y, 
                    differential=elevation_diff, 
                    is_child=True
                )

    return fire_grid


def update_fire_grid(
    current_fire_grid: np.ndarray, 
    elevation_grid: np.ndarray, 
    allowed_difference: int=2
) -> np.ndarray:
    """Update the fire grid for one time-step
    
    Args:
        current_fire_grid: The current grid with fire information.
        elevation_grid: The grid with the elevation information.
        allowed_difference: The criteria for fire to spread from pixel to another.

    Returns:
        The Fire grid for timestamp + 1
    
    """
    all_fire_indexes = np.argwhere(current_fire_grid)
    for x, y in all_fire_indexes:
        updated_fire_grid = spread_fire_for_location(
            fire_grid=current_fire_grid, 
            elevation_grid=elevation_grid, 
            location_x=x, 
            location_y=y, 
            differential=2, 
            is_child=False
        )

    return updated_fire_grid


def get_fake_elevation_grid():
    # Setting a fake elevation. 
    elevation_grid = np.zeros((10, 10)) + 3

    elevation_grid[4, 4] = 4 # Monotonically increasing
    elevation_grid[5, 5] = 6
    elevation_grid[5, 6] = 7
    elevation_grid[5, 7] = 9 # fire should not spread here in the first iteration.
    elevation_grid[5, 8] = 29 # fire should never spread here!
    return elevation_grid


def run_grow_example(timesteps=3):
    """Demo example of fire spreading through a terrain"""
    current_fire_grid = np.zeros((10, 10))
    current_fire_grid[4, 4] = 1

    # Just binarizing the array.
    current_fire_grid = current_fire_grid > 0.5
    elevation_grid = get_fake_elevation_grid()

    for timestep in range(timesteps):
        current_fire_grid = update_fire_grid(current_fire_grid, elevation_grid)
        assert current_fire_grid[5, 8] == False
        if timestep == 0:
            assert current_fire_grid[5, 6] == False
        else:
            assert current_fire_grid[5, 6] == True
        print(current_fire_grid)


if __name__ == "__main__":
    run_grow_example()
