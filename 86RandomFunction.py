import random

# สุ่มตัวเลข random()
print("# random 0.0-1.0")
x1 = random.random() # สุ่มตัวเลข 0.0 - 1.0
print(x1)

print("\n")

# สุ่มตัวเลขเเบบกำหนดช่วง uniform()
print("# random 5.0 - 10.0")
x2 = random.uniform(5,10) # 5 <= x <= 10 สุ่มในช่วง 5 - 10
print(x2)

print("\n")

# random.randrange(start,stop,step)
print("# random.randrange()")
for i in range(3):
    x = random.randrange(1,10,2) # พอระบุให้ step เป็น 2 จะสุ่มตัวเลข 1-10 เเต่เพิ่มรอบทีละสองก็จะได้เป็น สุ่ม 1,3,5,7,9 เเทน
    print(x, end=' ')

print("\n")

# random.choice()
print("# random.choice()")
items = [1, 2, 3, "A", "B", "C"]
for i in range(3):
    x = random.choice(items) # เขียนได้หลายเเบบ Ex. choice([1,2,3,"A","B","C"]) หรือ choice("123ABC") เป็นการลดรูปไม่ต้องเขียน list
    print(x, end=' ')

print("\n")

# random.shuffle(list)
print("old format items : ", items)
random.shuffle(items)
print("new format items : ", items)