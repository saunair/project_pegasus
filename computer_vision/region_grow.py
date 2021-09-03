from copy import copy

import numpy as np


def spread_fire_for_location(fire_grid, elevation_grid, location_x, location_y, differential, is_child=False):
    assert fire_grid[location_x][location_y], "Fire cannot spread from a location that hasn't been lit yet."
    
    if is_child is False:
        assert differential == 2, "Just keeping a sanity check as per the problem requirement. Diff {differntial}"

    x_len, y_len = fire_grid.shape
    if location_x == x_len or location_y == y_len or location_x < 0 or location_y < 0:
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
            elevation_diff = elevation_grid[location_x][location_y] - elevation_grid[location_x][current_y]

            # If the location is the root location, we can take the absolute to find the differential
            if np.abs(elevation_diff) <= differential and not is_child:
                fire_grid[current_x][current_y] = True
            if elevation_diff == differential and is_child:
                fire_grid[current_x][current_y] = True

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


def update_fire_grid(current_fire_grid, elevation_grid, allowed_difference=4):
    all_fire_indexes = np.argwhere(current_fire_grid)
    current_fire_grid = copy(current_fire_grid)

    for x, y in all_fire_indexes:
        current_fire_grid = spread_fire_for_location(
            fire_grid=current_fire_grid, 
            elevation_grid=elevation_grid, 
            location_x=x, 
            location_y=y, 
            differential=2, 
            is_child=False
        )

    return current_fire_grid


def run_grow_example(timesteps=1):
    current_fire_grid = np.zeros((10, 10))
    current_fire_grid[4, 4] = 1

    # Just binarizing the array.
    current_fire_grid = current_fire_grid > 0.5
    elevation_grid = np.zeros((10, 10))
    for timestep in range(timesteps):
        current_fire_grid = update_fire_grid(current_fire_grid, elevation_grid)
        print(current_fire_grid)



if __name__ == "__main__":
    run_grow_example()
