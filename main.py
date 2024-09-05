# Decorator = A function that extends the behavior of another fucntion
#             w/o modifying the base function
#             Pass the base function as an argument to th decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

# *****************************
# * decorator function 패턴
# *****************************
# def decorate_function(func): # func는 base function을 말한다.
#     def wrapper():
#         func()
#
#     return wrapper


# *****************************
# * 기본적인 사용 방법
# *****************************
# def add_sprinkles(func):
#     def wrapper():
#         print("*You add sprinkles 🥨")
#         func()

#     return wrapper

# *base 함수위에 @decorate 함수명(add_sprinkles)을 삽입해야한다.
# @add_sprinkles
# def get_ice_cream():
#     print("Here is your ice cream 🍦")


# *****************************
# * base 함수에 인자가 없을 때
# *****************************
# def add_sprinkles(func):
#     def wrapper():
#         print("*You add sprinkles 🥨")
#         func()

#     return wrapper


# def add_choco(func):
#     def wrapper():
#         print("*You add choco 🍫")
#         func()

#     return wrapper


# @add_sprinkles
# @add_choco
# def get_ice_cream():
#     print("Here is your ice cream 🍦")


# *****************************
# * base 함수에서 인자가 있을때
# *****************************

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🥨")
        func(*args, **kwargs)

    return wrapper


def add_choco(func):
    def wrapper(*args, **kwargs):
        print("*You add choco 🍫")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_choco
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")


get_ice_cream("Vanila")
