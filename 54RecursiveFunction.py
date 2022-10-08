# recursive function คือ function ที่มีการเรียกใช้ function ตัวมันเอง

'''
Ex.

def a():
    print("A")
    a() # เรียกใช้ function ตัวมันเอง จะรันต่อเนื่องไม่มีที่สิ้นสุด ดังนั้นต้องหาจุดออก
'''

'''
Trik

หาจุดวนซ้ำ
หาจุดออกจาก function (return)
ต้องมี parameter
'''

''' Ex. print 1-5 โดยห้ามใช้ loop '''

# function

def addNumber(number):
    if number == 5:
        return # จุดออกจาก function
    print(number+1)
    number = number+1
    addNumber(number) # จุดวนซ้ำ

# main program
addNumber(0)