# Change Data In List
numbers1 = [1, "Napat", True, 3.9] # List
print("Before = ", numbers1[0])
numbers1[0] = 2
print("After = ", numbers1[0])
print("------------------------------")

# Change data in tuple
''' 
Tuple cannont change data like List
tup[0] = 45 Wrong !!!
'''
tup = (2, False, 'C', 1.56) # Tuple
print("old tuple = ", tup)

# ถ้าจะเเก้ให้เเปลงเป็น List โดยสร้าง List ใหม่ขึ้นมาเเล้วยัดข้อมูลลงไป
lis = list(tup)
print(lis)

# จากนั้นเเปลงค่าตามที่ต้องการผ่าน lis
lis[0] = "Bangkok"

# update List => Tuple
tup = tuple(lis)
print("new tuple = ", tup)
