# สร้างเเละ กำหนด Exception เอง ด้วย raise
# ต้องเขียนภายใต้ block try 

while True:
    try:
        name = input("Enter username : ")
        if name == "pim":
            raise Exception("you account is banded")
        number1 = int(input("Enter number1 : "))
        number2 = int(input("Enter number2 : "))
        if number1<0 or number2<0:
            raise Exception("Enter positive number")
        result  = number1/number2
        print(result)
        break
    except Exception as e:
        print(e)
    finally:
        print("I don't care")
        print("----------------------")