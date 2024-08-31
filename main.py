
# name = input("Enter your full name: ")


# phone_number = input("Enter your phone number: ")

# name = Bro Code
# result = len(name) # 8
# result = name.find("o") # 2
# result = name.rfind("o") # 5
# result = name.find("q") # 문자가 없으면 -1

# name = name.capitalize() # bro code -> Bro code
# name = name.upper() # bro code -> BRO CODE
# name = name.lower() # BRO coDE -> bro code

# result = name.isdigit() #Bro ->False, Bro123->False, 123->True
# result = name.isalpha()  # 문자열일때만 True, 공백문자도 False

# result = phone_number.count("-") # 문자열에서 해당문자 개수 리턴
# result = phone_number.replace("-", " ")  # 문자열에서 해당문자를 특정문자로 변경


# print(help(str))

# Exercise: validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("username is no more than 12 characters")
elif not username.find(" ") == -1:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print(f"Welcome {username}")
