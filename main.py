# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusuable separate files


# 모듈 사용법
# import math
# import math as m # m is alias
# from math import pi # not recommend

import example

# result = example.pi
# result = example.square(3)
# result = example.cube(3)
result = example.circumference(3)
result = example.area(3)
print(result)
