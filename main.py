# object = A "bundle" of related attributes(variables) and methods(functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

cars = [car1, car2, car3]

# for car in cars:
#     print(car.model)
#     print(car.year)
#     print(car.color)
#     print(car.for_sale)
#     print("*****************")

# car1.drive()
# car1.stop()
# car2.drive()
# car2.stop()
