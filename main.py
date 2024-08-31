# indexing = accessing elements of a sequence using [] (aka indexing operator)
#           [start : end(exclusive) : step]

credit_number = "1234-5678-9012-3456"
# index:         0123456789
# index:                      -4-3-2-1


# print(credit_number[0])

# print(credit_number[0:4])  # 1234
# print(credit_number[:4])  # 1234
# print(credit_number[5:9])  # 5678
# print(credit_number[5:])  # 5678-9012-3456
# print(credit_number[::2])  # 13-6891-46

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

backward_cc_number = credit_number[::-1]
print(backward_cc_number)
