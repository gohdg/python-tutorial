# super() = Function used in a child class to call methods from a parent class (super class).
#           Allows you to extend the functionality of the inherited methods

from turtle import circle, width


class Shape:
    def __init__(self, color, is_filled) -> None:
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {
              'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius
    # override

    def describe(self):
        super().describe()  # extend functionality
        print(f"It is a circle with an area of {
              3.14 * self.radius * self.radius}")


class Square(Shape):
    def __init__(self, color, is_filled, width) -> None:
        super().__init__(color, is_filled)
        # self.color = color
        # self.filled =filled
        self.width = width

    def describe(self):
        super().describe()  # extend functionality
        print(f"It is a square with an area of {
              self.width * self.width}")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height) -> None:
        super().__init__(color, is_filled)
        # self.color = color
        # self.filled =filled
        self.width = width
        self.height = height

    def describe(self):
        super().describe()  # extend functionality
        print(f"It is a triangle with an area of {
              self.width * self.height / 2}")


circle = Circle("red", True, 5)
print(circle.color)

square = Square(color="blue", is_filled=False, width=6)
print(square.color)

triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)
print(triangle.width)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()
