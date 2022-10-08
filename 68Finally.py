# Finally จะทำงานเสมอไม่สนใจว่า program จะ error มั้ย

try:
    number1 = int(input("Enter number1 : "))
    number2 = int(input("Enter number2 : "))
    result  = number1/number2
    print(result)
except Exception as e:
    print(e)
finally:
    print("I don't care")