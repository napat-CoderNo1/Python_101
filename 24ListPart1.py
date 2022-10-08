# primitive
# อยากใช้ตัวเลข 5 ตัวมาทำงาน
# ก็ต้องสร้างตัวเเปร 5 ตัวมาเก็บค่า
'''
a1 = 17
a2 = 26
a3 = 15
a4 = 999
a5 = 345
'''
# ใช้ Non-primitive เเทน
# สร้างตัวเเปร1ตัวเก็บได้หลายค่า (ยังไงวะ??) เริ่มเรียนจาก List

# Non-primitive : List

# การนิยาม ใช้ []
number1=[]                       # list ว่าง
number2=[1,2,3,4,5,6]            # list มีสมาชิก คือ 1,2,3,4,5,6
name=["Mr.A","Mr.B","Mr.C"]      # list มีสมาชิกเป็น string
all=[10,"Mr.Egg",True,3.14,-10]  # list เก็บข้อมูลต่างชนิดกันได้

# constructor ประกาศเลยว่าใช้ list
name2=list(["Mr.Ant","Mr.B"])

print(name)     # print all data in list name
print(name2[0]) # print only Mr.Ant
