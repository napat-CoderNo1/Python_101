# try except structure
'''
try:
   คำสั่งในการรันโปรเเกรมปกติ
except:
    คำสั่งที่ทำงานตอนโปรเเกรมผิดพลาด 
'''

try:
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    result  = number1/number2
    print(result)
except:
    print("Program Error")