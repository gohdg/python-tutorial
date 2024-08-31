# format specifiers = f"{value:flags}"

# .(number)f = round to that many decimal places (fixed point)
# :(number) = 공백 추가
# :03 = allocate and zero pad that many spaces
# :< = 왼쪽 정렬 default
# :> = 오른쪽 정렬
# :^ = 가운데 정렬
# :+ = 양수 표시
# : = 양수 앞에 공백추가
# :, = 숫자에 comma 추가

price1 = 3.14659
price2 = -987.65
price3 = 12.34

price4 = 12000.14659
price5 = -9870.65
price6 = 1200.34

print(f"Price 1 is {price1:.2f}")  # 3.15
print(f"Price 2 is {price2:.2f}")  # -987.65
print(f"Price 3 is {price3:.2f}")  # 12.34

print(f"Price 1 is ${price1:.1f}")  # $3.1
print(f"Price 2 is ${price2:.1f}")  # $-987.6
print(f"Price 3 is ${price3:.1f}")  # $12.3

# :(number) = 공백 추가, number는 자리수
print(f"Price 1 is ${price1:10}")  # $   3.14659
print(f"Price 2 is ${price2:10}")  # $   -987.65
print(f"Price 3 is ${price3:10}")  # $     12.34

# :0(number) = 0으로 추가, number는 자리수
print(f"Price 1 is ${price1:010}")  # $0003.14659
print(f"Price 2 is ${price2:010}")  # $-000987.65
print(f"Price 3 is ${price3:010}")  # $0000012.34

# :<(number) = 왼쪽정렬, number는 자리수
print(f"Price 1 is ${price1:<10}")  # $3.14659
print(f"Price 2 is ${price2:<10}")  # $-987.65
print(f"Price 3 is ${price3:<10}")  # $12.34

# :>(number) = 오른쪽정렬, number는 자리수
print(f"Price 1 is ${price1:>10}")  # $   3.14659
print(f"Price 2 is ${price2:>10}")  # $   -987.65
print(f"Price 3 is ${price3:>10}")  # $     12.34

# :^(number) = 가운데정렬, number는 자리수
print(f"Price 1 is ${price1:^10}")  # $  3.14659
print(f"Price 2 is ${price2:^10}")  # $ -987.65
print(f"Price 3 is ${price3:^10}")  # $   12.34

# :+ = 양수 표시
print(f"Price 1 is ${price1:+}")  # $+3.14659
print(f"Price 2 is ${price2:+}")  # $-987.65
print(f"Price 3 is ${price3:+}")  # $+12.34

# : = 양수일경우 앞에 공백
print(f"Price 1 is ${price1: }")  # $ 3.14659
print(f"Price 2 is ${price2: }")  # $-987.65
print(f"Price 3 is ${price3: }")  # $ 12.34

# :, = 1000단위 comma 표시
print(f"Price 4 is ${price4:,}")  # $12,000.14659
print(f"Price 5 is ${price5:,}")  # $-9,870.65
print(f"Price 6 is ${price6:,}")  # $1,200.34

# :+,.2f = 양수기호 표시, 1000단위 comma 표시, 소수점 2자리까지
print(f"Price 4 is ${price4:+,.2f}")  # $+12,000.15
print(f"Price 5 is ${price5:+,.2f}")  # $-9,870.65
print(f"Price 6 is ${price6:+,.2f}")  # $+1,200.34
