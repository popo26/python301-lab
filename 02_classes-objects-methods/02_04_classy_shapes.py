# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle():
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def rec_area(self):
        area = self.length * self.width
        print(area)

    def rec_perimeter(self):
        perimeter = self.length * 2 + self.width * 2
        print(perimeter)


class Circle():
    def __init__(self,radius) -> None:
        self.radius = radius
        
    def cir_area(self):
        area = 3.14 * self.radius ** 2
        print(area)

    def cir_circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(circumference)

rec = Rectangle(1,5)
cir = Circle(10)

rec.rec_area()
rec.rec_perimeter()
cir.cir_area()
cir.cir_circumference()

