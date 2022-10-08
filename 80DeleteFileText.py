import os

try:
    if os.path.exists("forDelete.txt"):
        os.remove("forDelete.txt")
        print("file deleted")
    else:
        print("file not found")
except Exception as e :
    print(e)