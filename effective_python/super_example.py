class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# An example for Super for parent construction.
class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class VolumeMixin:
    @property
    def volume(self):
        return self.surface_area *  self.height       


class Cuboid(Rectangle, VolumeMixin):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        super(Rectangle, self).__init__(length, breadth)
    
    @property
    def surface_area(self):
        """Total surface area is a sum of each side's area, multiplied by two"""
        return 2*((super().area()) + (self.breadth*self.height) + (self.length*self.height))


class Cube(Cuboid): 
    def __init__(self, length):
        super(Cuboid, self).__init__(length, length, length)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def triangle_area(self):
        """ Half * base * height"""
        return 0.5 * self.base * self.height


class Pyramid(Square, Triangle):
    def __init__(self, base_length, slant_height):
        self.base_length = base_length
        self.slant_length = slant_height
        super(Square, self).__init__(base_length)

    @property
    def volume(self):
        return (super().area  + self.triangle_area) * self.slant_height
