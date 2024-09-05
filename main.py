# Python file detection

# os.path.exists(file_path)
# os.path.isfile(file_path)
# os.path.isdir(file_path)
# os.path.join(dir, dir, filename)
# os.path.expanduser("~") // home directry

import os

home_dir = os.path.expanduser("~")

file_path = home_dir + "/PCCMW/pcc.config"
file_path = os.path.join(home_dir, "PCCMW", "pcc.config")
file_path = os.path.join(home_dir, "PCCMW")

print(file_path)

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")
