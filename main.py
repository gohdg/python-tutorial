# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"

# 상속을 통한 polymorphism과 달리, 상속을 받지 않은 클래스에서 동일한 이름의 속성/메서드가 있으면 polymorphism을 구현할 수 있는 방법

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:  # 상속 받지 않는다.
    alive = False

    def speak(self):
        print("HONK!")


animals = [Dog(), Cat(), Car()]  # polimorphism 구현

for animal in animals:
    animal.speak()
    print(animal.alive)
