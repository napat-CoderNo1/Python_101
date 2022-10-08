# รวมสมาชิกใน list
number = [1,2,3]
name = ["napat","Anna","Jew"]

all = number+name
print("list all: ",all)

# การทำเเบบนี้จะสร้าง list all ขึ้นมาใหม่เพื่อเก็บข้อมูล

# ถ้าใช้ extend() จะเป็นการนำข้อมูลของอีก list มาใส่ โดยไม่ต้องสร้าง list ใหม่
print("List number before extend: ",number)
number.extend(name)
print("List number after extend: ",number)