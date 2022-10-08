# find Max and Min Number

n = int(input("Enter Amount of Number: "))
while n<2:
    print("Please Enter At Least 2 Number: ")
    n = int(input("Enter Amount of Number: "))

i=1
while i<=n:
    number = int(input("Enter Number: "))

    if i==1:
        max = number
    if i==2:
        if number>max:
            min = max
            max = number
        elif number<max:
            min = number
        else:
            min = number
    if i>=3:
        if number>max:
            max = number
        elif number<min:
            min = number
        else:
            pass

    i+=1

print("Max: ",max)
print("Min: ",min)