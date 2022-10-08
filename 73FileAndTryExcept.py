try:
    fr2 = open("Xstudent.txt", "r", encoding="utf-8") # เขียนชื่อไฟล์ผิด
    print(fr2.read())
except FileNotFoundError :
    print("file not found")