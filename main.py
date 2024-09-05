# Magic methods = Dunder methods (double underscore methods)
#                 __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customzie the behavior of objects


class Book:

    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # print(book1) 하면 보통 메모리 주소를 출력하는데, 아래 __str__를 정의하면 메모리주소 대신의 정의한 대로 출력된다.
    def __str__(self):
        return f"'{self.title}' by {self.author} "


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowlling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
