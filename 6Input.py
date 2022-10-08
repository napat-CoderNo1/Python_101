# format1 รับค่าที่ user ป้อนเเล้วเก็บลงตัวเเปร name1
name1 = input()
print(name1)        # show result

print(type(name1))  # type is automatically assigned to str.

# format2
name2 = input("Enter your name : ")
print("Your name is : " + name2)

# ตัว input รับค่ามาเป็น string เท่านั้น ถ้าต้องการให้ + กันได้ต้องเเปลงก่อน

#-----------------------------------------------------------------

# เเปลงที่ขั้นตอน process

#input
x = input("Enter 1st Number : ")
y = input("Enter 2nd Number : ")
#process
z = int(x)+int(y) 
#output
print("Number1+Number2 = " + str(z))

#-----------------------------------------------------------------

# เเปลงที่ขั้นตอน input
#input
x = int(input("Enter 1st Number : "))
y = int(input("Enter 2nd Number : "))
#process
z = x+y
#output
print("Number1+Number2 = " + str(z))
print("Number1+Number2 = " , z)       # same result to above line