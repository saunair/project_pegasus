from copy import copy

import numpy as np
from fire import Fire
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


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


def get_fake_elevation_grid(
    num_rows: int = 20,
    num_columns: int = 20,
) -> np.ndarray:
    """An elevation grid that can be used for testing purposes.
    
    Args:
        num_rows:
        num_columns:

    Returns:
        An elevation grid that has some monotonically 
        increasing and discontinuous terrain that will not let fire spread.
    
    """
    # Setting a fake elevation. 
    elevation_grid = np.zeros((num_rows, num_columns)) + 3

    elevation_grid[4, 4] = 4 # Monotonically increasing
    elevation_grid[5, 5] = 6
    elevation_grid[5, 6] = 7
    elevation_grid[5, 7] = 9 # fire should not spread here in the first iteration.
    elevation_grid[5, 8] = 29 # fire should never spread here!
    return elevation_grid


def get_mountain_grid(
    num_rows: int = 20,
    num_columns: int = 20,
    add_discontinuity: bool = True,
) -> np.ndarray:
    """Setting a gaussian line elevation.
    
    Args:
        num_rows: 
        num_columns:

    Returns:
        A two dimensional grid that emulates the elevatino of a mountain/hilly area.
    
    """
    elevation_grid = np.zeros((num_rows, num_columns))
    for row in range(num_rows):
        for column in range(num_columns):
            elevation_grid[row, column] = np.sqrt((num_rows)**2 - (num_rows/2 - row)**2 - (num_columns/ 2 - column)**2)
    
    # Just to add some discontinuous gradient.
    if add_discontinuity:
        elevation_grid[int(0.8*num_rows), :] = np.max(elevation_grid) 

    return elevation_grid


def run_grow_example(
    timesteps: int =5, 
    num_rows: int = 20, 
    num_columns: int = 20, 
    is_test: bool = False, 
    plot: bool = False
) -> None:
    """Demo example of fire spreading through a terrain.
    
    Args:
        timesteps: Number of time steps we are running this simulation over.
            Each timestep is a single unit of time. There is no concept of unit of time here. 
        num_rows: Number of rows in the grid
        num_columns: Number of columns in the grid
        is_test: True if we are running it over a fake elevation for testing purposes.
            False if this is running on a gaussian like elevation grid.
        plot: True if the output and the grid needs to be plotted.
    
    """
    current_fire_grid = np.zeros((num_rows, num_columns))
    current_fire_grid[4, 4] = 1

    # Just binarizing the array.
    current_fire_grid = current_fire_grid > 0.5

    if is_test:
        elevation_grid = get_fake_elevation_grid(
            num_rows=num_rows, 
            num_columns=num_columns
        )
    else:
        elevation_grid = get_mountain_grid(
            num_rows=num_rows, 
            num_columns=num_columns
        )

    elevation_graph = go.Heatmap(z=elevation_grid.tolist())
    fig = go.Figure(data=elevation_graph)
    fig.update_layout( title="elevation map")
    fig.show()

    for timestep in range(timesteps):
        fig = go.Figure(go.Heatmap(z=(current_fire_grid * 1.0).tolist()))
        fig.update_layout(title=f"Fire at timestep {timestep}")
        fig.show()
        current_fire_grid = update_fire_grid(current_fire_grid, elevation_grid)
        # Just some test cases to verify.
        if is_test:
            assert current_fire_grid[5, 8] == False
            if timestep == 0:
                assert current_fire_grid[5, 6] == False
            else:
                assert current_fire_grid[5, 6] == True
    
    fig = go.Figure(go.Heatmap(z=(current_fire_grid * 1.0).tolist()))
    fig.show()


if __name__ == "__main__":
    Fire(run_grow_example)
