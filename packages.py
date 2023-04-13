# import os
import shutil
# print(os.getcwd())
# print(shutil.disk_usage("/"))
total, used, free = shutil.disk_usage("/")
# print("Total total: ", total // 2**30, "GB")
# print("Total used: ", used // 2**30, "GB")
# print("Total free: ", free // 2**30, "GB")

# Using f String
print(f"Total total: {total // 2**30} GBs")
print(f"Total used: {used // 2**30} GBs")
print(f"Total free: {free // 2**30} GBs")
