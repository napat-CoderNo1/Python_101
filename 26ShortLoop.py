# Ass4 shortly for loop

number = [1,2,3,4,5]
print(number)

# normal
for i in range(len(number)):
    number[i] = number[i]**2
print(number)

# shortly
number = [i*i for i in number]
print(number)