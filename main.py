# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes/methods

# 각각의 클래스가 동일 이름의 메서드를 가지고 있을때 각 클래스를 List화 해서 for loop로 호출하는 것

from abc import ABC, abstractmethod


class Shape(ABC):  # ABC를 상속 받으면 추상 클래스가 된다.

    @abstractmethod  # abstratmethod decorator 를 선언 sub class는 반드시 구현해야 한다
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):  # Circle 을 상속하면 area 메소드를 사용할 수 있게 되어 아래 list에 담아 사용할 수 있어 Circle를 상속 받음
    def __init__(self, topping, radius) -> None:
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")
