# Factorial

def factorial(number):
    if number == 0:
        return
    if number == 1:
        print(number, end='')
    else:
        print(number, "x ", end='')
    number = number-1
    factorial(number)

def factorialAns(number):
    if number == 1:
        return number
    else:
        return number * factorialAns(number-1)

def factorialShow(number):
    print(number,"! = ", end='')
    factorial(number)
    print(" = ", end='')
    print(factorialAns(number), end='')

factorialShow(4)