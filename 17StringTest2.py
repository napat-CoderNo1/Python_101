''' Temperature unit converter 2 '''

temp = input("Enter degree and unit : ") # EX. 45F
print(temp[:-1])
degree = int(temp[0:-1])
unit = temp[-1].upper() # ตัวสุดท้าย(ตัวเเรกนับจากด้านหลัง) , upper() => เเปลงเป็น ตัวพิมพ์ใหญ่เผื่อผู้ใช้ป้อนตัวเล็กมา

if unit == 'C' :
    print((degree*(9/5))+32,'F')

if unit == 'F' :
    print((degree-32)*(5/9),'C')