# exception = An event thatt interrups the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally
# try:
#     pass
#     # Try some code
# except Exception:
#     pass
#     # Handle an Exception
# finally:
#     pass
#     # Do some clean up


try:
    number = int(input("Enter a number: "))
    print(1/number)
except Exception as ex:
    print(f"Error {ex}")
finally:
    print("bye")
