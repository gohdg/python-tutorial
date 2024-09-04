# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position

    # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    # static method
    @staticmethod
    def is_valid_position(position):  # no need self keyword
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# class와 instance에서 모두 접근 가능
print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.is_valid_position(employee1.position))
