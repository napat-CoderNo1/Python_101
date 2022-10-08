# Anonymous,lambda function => function has no name

'''
Structure

lambda arguments : expression

'''
# x จะกลายเป็นชื่อ function ตอนเรียกใช้
x = lambda name:name # เขียนเเบบนี้เท่ากับเป็นการ return name ออกมาโดยอัตโนมัติ

print(x("Napat")) # Napat เป็น Arguments ที่ส่งค่าไปใน parameter name เเล้ว function ก็จะ return ค่า name = Napat ออกมา

print("\n")

# Ex.2
sum = lambda x,y : x+y # return x+y
print(sum(2,3))

print("\n")

# Ex.3
multiply = lambda a,b : a*b # return a*b
result = multiply(5, 10)
print(result)