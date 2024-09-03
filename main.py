# Match-case statement

# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Not a valid day"


# print(day_of_week(1))


# def day_of_week2(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valida day"


# print(day_of_week2(1))


# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _:
#             return False


# print(is_weekend("Friday"))


def is_weekend2(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False


print(is_weekend2("Saturday"))
