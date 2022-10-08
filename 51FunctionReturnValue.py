'''
Type of Function

1. ไม่มีการรับค่า เเละ ส่งค่า

def name():
    statement

2. มีการส่งค่าเข้าไปทำงาน

def name(parameter):
    statement

3. มีการรับค่าเเละ return ค่าออกมา

def name(parameter):
    return value

4. ไม่มีการรับค่าเข้ามา เเต่มีการ return ค่าออกไป

def name():
    return value

'''

def add(a,b):
    return a+b

add(10,5) # not print anything
print("add(10,5) = ", add(10,5))

print("\n")

def showNumber():
    return 500

showNumber() # not print anything
print("showNumber() = ", showNumber())