# function

def displayFruit(item):
    print(item)

def displayFruit2(item):
    for i in range(len(item)):
        print("fruit number ", i, " = ", item[i])

# main program
fruit = ["mango", "apple"] # ส่งข้อมูลที่เป็น list/tuple ไปใน function ได้

displayFruit(fruit)
print("\n")
displayFruit2(fruit)