# เมื่อไม่มี error ใช้ else จะให้ทำอะไรต่อ
# ถ้า program error จะไม่เข้า else

try:
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    result  = number1/number2
    print(result)
except Exception as e:
    print(e)
else:
    print("End program")