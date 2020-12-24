class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class VolumeMixin:
    @property
    def volume(self):
        return self.surface_area *  self.height       


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class Cuboid(Rectangle, VolumeMixin):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

        super(Rectangle, self).__init__(length, breadth)
    
    @property
    def surface_area(self):
        return 2*((self.length*self.breadth) + (self.breadth*self.height) + (self.length*self.height))


class Cube(Square): 
    @property
    def surface_area(self):
        return super(Square, self).area()
    

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def triangle_area(self):
        return 0.5 * self.base * self.height


class Pyramid(Square, Triangle):
    def __init__(self, base_length, slant_height):
        self.base_length = base_length
        self.slant_length = slant_height
        super(Square, self).__init__(base_length)

    @property
    def volume(self):
        return (super().area  + self.triangle_area) * self.slant_height
