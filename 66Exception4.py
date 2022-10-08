# เมื่อไม่รู้ว่าจะเกิด error อะไร ใช้วิธีนีเพื่อให้โปรเเกรมบอกเรา

try:
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    result  = number1/number2
    print(result)
except Exception as e:
    print(e)