# @property = Decorator used to define a method as a property (it can be accesed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             메서드이기도 하고 접근은 속성처럼 하니까 속성값을 읽거나, 변경하거나, 삭제하고자 할때 메서드에서 어떤 로직을 적용할 수가 있다.
#
#             Gives you getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(3, 4)

print(rectangle.width)  # 3
print(rectangle.height)  # 4


class Rectangle1:
    def __init__(self, width, height):
        self._width = width  # _변수, private 변수를 만드는법, __변수 강제 private 진짜 접근 안됨
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # setter 정의하기
    @width.setter
    def width(self, new_width):  # property method의 이름과 일치해야한다
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):  # property method의 이름과 일치해야한다
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle1(3, 4)

rectangle.width = 30
rectangle.height = 20

# print(rectangle.width)  # 3.0cm
# print(rectangle.height)  # 4.0cm

# 속성 메서드를 삭제, 속성자체가 삭제 되니까, 이후 접근이 안된다.
del rectangle.width
del rectangle.height
