import pytest

from super_example import Cube


@pytest.mark.unit
def test_cube():
    box_cube = Cube(5.)
    assert box_cube.surface_area == 25
    assert box_cube.volume == 125


