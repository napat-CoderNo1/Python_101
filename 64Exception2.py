'''
ข้อผิดพลาดมีหลายเเบบ
1. ValueError ใส่ข้อมูลที่เป็นคนละชนิดกับที่โปรเเกรมให้ป้อน
2. ZeroDivisionError เอา 0 ไปหาร ตัวเลข
'''

try:
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    result  = number1/number2
    print(result)
except ValueError:
    print("Enter only data type int")
except ZeroDivisionError:
    print("Program must be error if you division by 0") 
