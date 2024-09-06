# Python reading files (.txt, .json, .csv)

import os
import json
import csv

home_dir = os.path.expanduser("~")

#  ************************************
#  * read txt file
#  * mode="r"
#  ************************************

# file_path = os.path.join(home_dir, "Desktop", "output.txt")

# try:
#     with open(file=file_path, mode="r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")
# except Exception as ex:
#     print(f"Error occurred during reading a file: {ex}")

# ************************************
# * read json file
# * mode="r"
# * import json
# * json.load(file): return object
# ************************************
# file_path = os.path.join(home_dir, "Desktop", "input.json")
# try:
#     with open(file=file_path, mode="r") as file:
#         content = json.load(file)
#         print(content)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")
# except Exception as ex:
#     print(f"Error occurred during reading a file: {ex}")

# ************************************
# * read csv file
# * mode="r"
# * import csv
# * csv.reader(file): return list collection,한줄 한줄 리스트
# * csv 파일은 row 에 list가 있다고 생각하면 된다.
# * 각 list의 item은 column 이 된다.
# ************************************
file_path = os.path.join(home_dir, "Desktop", "input.csv")
try:
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)  # row를 출력
            print(line[0])  # 각 row의 0번째 column을 출력
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
except Exception as ex:
    print(f"Error occurred during reading a file: {ex}")
