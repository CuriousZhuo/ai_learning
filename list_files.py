import os

folder_path = "./test_files"

all_files = os.listdir(folder_path)

for name in all_files:
    print(name)
