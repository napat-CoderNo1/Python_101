def displayNumber():
    x = 10       # Local Variable
    print("Hello = ", x)

# main program
x = 20           # Global Variable
displayNumber()
print("Hello = ", x)