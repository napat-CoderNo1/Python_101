# find Max and Min Number

number1 = int(input("Enter Number1: "))
number2 = int(input("Enter Number2: "))
number3 = int(input("Enter Number3: "))
number4 = int(input("Enter Number4: "))

max = number1

if number2>number1:
    max = number2
    min = number1
elif number2<number1:
    min = number2
else:
    min=number2

if number3 > max:
    max = number3
elif number3 < min:
    min = number3
else:
    pass

if number4 > max:
    max = number4
elif number4 < min:
    min = number4
else:
    pass

print("Max: ",max)
print("Min: ",min)