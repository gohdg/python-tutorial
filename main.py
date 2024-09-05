# Python writing file (.txt, .json, .csv)

# os.path.exists(file_path)
# os.path.isfile(file_path)
# os.path.isdir(file_path)
# os.path.join(dir, dir, filename)
# os.path.expanduser("~") // home directry

# ******************************
# * write txt file
# ******************************

# import os

# home_dir = os.path.expanduser("~")
# file_path = os.path.join(home_dir, "Desktop", "output.txt")

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# with open(file=file_path, mode="w") as file:
#     for employee in employees:
#         file.write(employee + "\n")

#     print(f"txt file {file_path} was created")


# ******************************
# * write json file
# * import json
# * json.dump(object, file stream, indent=4)
# * json.dump: object를 json string으로 바꾸고 파일저장. indent를 줘서 예쁘게 표현
# ******************************

# import os
# import json

# home_dir = os.path.expanduser("~")
# file_path = os.path.join(home_dir, "Desktop", "output.json")

# employees = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

# with open(file=file_path, mode="w") as file:
#     json.dump(employees, file, indent=4)
#     print(f"txt file {file_path} was created")

# ******************************
# * write csv file (comma seperated value)
# * import csv
# * open(, , newline="")을 사용해서 줄바꿈이 추가적으로 생기지 않게 해야한다.
# ******************************

import os
import csv

home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "Desktop", "output.csv")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

with open(file=file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)

    print(f"txt file {file_path} was created")
