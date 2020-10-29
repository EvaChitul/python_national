'''We have new customers for our Polygons company.
    They need to create square objects with a certain area
    They need a method to compute the perimeter only for triangle objects
Requirements:
    add an alternative constructor to Square class that takes the area as an argument and creates a square object with the apropriate sides
    example :
    >> sq = Square.from_area(8)
    >> print(sq)
    >> Side 1 with lenght: 2
    >> Side 2 with lenght: 4
    >> Side 3 with lenght: 2
    >> Side 4 with lenght: 4
    we want to make our perimeter method also available to other shapes in the future. Create a mixin class for perimeter that contains the perimeter method
'''
from math import sqrt
import random


class Polygon:
    def __init__(self, *args):
        self.sides = list(args)

    def __str__(self):
        return f'Polygon object has {len(self.sides)} sides'

    def display(self):
        for index, side in enumerate(self.sides, start=1):
            print(f'Side {index} with length: {side}')


class PerimeterMixin(Polygon):
    def __init__(self, *args):
        super().__init__(*args)

    def perimeter(self):
        full_perimeter = sum(self.sides)
        return f'Perimeter of {type(self).__name__} is: {full_perimeter}'


class Triangle(PerimeterMixin, Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def area(self):
        semi_perimeter = sum(self.sides) / 2
        return (semi_perimeter *(semi_perimeter - self.sides[0]) * (semi_perimeter - self.sides[1]) * (semi_perimeter - self.sides[2])) ** 0.5


class Square(Polygon):
    def __init__(self, side):
        super().__init__(side[0], side[1], side[2], side[3])

    def area(self):
        return self.sides[0] ** 2

    @classmethod
    def from_area(cls, area):
        sides_options = [(elem, int(area/elem)) for elem in range(1, int(sqrt(area))) if area % elem == 0]
        sides = random.choice(sides_options) * 2
        return cls(sides)

    def __str__(self):
        super().display()
        return 'The End'


tri = Triangle(10, 11, 30)
print(tri.perimeter())

tri_second = Triangle(5, 7, 30)
print(tri_second.perimeter())

sq = Square.from_area(50)
print(sq)
print(Square.from_area(13))
print(Square.from_area(29))
print(Square.from_area(30))