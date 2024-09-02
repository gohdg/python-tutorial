
# *******************************************************************************
# ** function = A block of reusuable code
# ** 실행방법: 함수명에 ()를 사용
# ** 함수선언: def 함수명():
# *******************************************************************************


# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Bro", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 142.50, "01/02")

# *******************************************************************************
# ** return = statement used to end a function
# **          and send a result back to the caller
# *******************************************************************************

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last


# full_name = create_name("bro", "code")
# print(full_name)

# *******************************************************************************
# ** default arguments = A default value for certain parameters
# **                     해당인자를 전달하지 않았을 때 사용
# **                     make your functions more flexible, reduces # of arguments
# **                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitrary
# *******************************************************************************

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# # print(net_price(500, 0, 0.05))
# # print(net_price(500))
# # print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# *******************************************************************************
# ** keyword arguments = an argument preceded by an identifier
# **                     helps with readability
# **                     argument의 순서는 문제가 되지 않는다
# **                     1. positional, 2.default, 3. KEYWORD, 4. arbitrary
# *******************************************************************************

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")


# # positional arguments way
# hello("Hello", "Mr.", "Spongebob", "Squarepants")
# # keyword arguments way
# hello("Hello", first="Spongebob", last="Squarepants", title="Mr.")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"


# phone_num = get_phone(country="82", area="10", first="7702", last="0809")
# print(phone_num)


# *******************************************************************************
# ** *args    = allow you to pass multiple non-key arguments
# ** **kwargs = allow you to pass multiple keyword arguments                      helps with readability
# **            * unpacking operator
# **            1. positional, 2.default, 3. keyword, 4. ARBITRARY
# *******************************************************************************

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="112 Fake St.",
#               city="Detroit",
#               state="MI",
#               zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321"
               )
