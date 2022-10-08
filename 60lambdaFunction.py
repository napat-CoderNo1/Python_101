# ใช้ lambda function คู่กับ function ปกติ

# เเบบปกติ
def myPower(x):
    return x*x

y = myPower(5)
print(y)

print("\n")

# เบบใช้ร่วมกัน
def myPower2(x):
    # x คือตัว arguments ของ myPower2
    # a คือตัว arguments ของ lambda function 
    return lambda a : x**a

z = myPower2(5)
result = z(2)
print(result)

'''
อธิบาย

z = myPower2(5) => ดูที่ myPower2(5) จะ return ออกมาเป็น function lambda ดังนั้น
z = lambda a : 5**a
z กลายเป็นฟังก์ชันเเลมดา ที่มี arguments คือ a

result = z(2) => a=2
result = 5**2 = 25
'''