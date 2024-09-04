# class variables = Shared among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age) -> None:
        self.name = name  # instance variable
        self.age = age  # instance variable
        Student.num_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

# class 변수 접근은 intance에서도 접근 되고, 클래스명으로도 접근된다.
# class 변수 접근법: instance.클래스 변수
print(student1.name)
print(student1.age)
print(student1.class_year)  # 2024, 공유되고 있다

print(student2.name)
print(student2.age)
print(student2.class_year)  # 2024, 공유되고 있다

# class 변수 접근법: 클래스명.클래스 변수
print(Student.class_year)

print(f"# of students: {Student.num_students}")  # of students: 2
