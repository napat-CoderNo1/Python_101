def addition(*args):
    total = 0
    for i in range(len(args)):
        total += args[i]
    print("sum = ", total)


def subtraction(num1, num2):
    print(abs(num1-num2))


def power(num1, m):
    print("ผลลัพธ์ = ", num1**m)


PI = 3.142857
Root2 = 1.414