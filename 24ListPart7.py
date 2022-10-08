# Delete Data From List

# remove()
cars = ["lambo","ferrari","ford","honda"]
print(cars)
cars.remove("lambo")
print(cars)

print("\n")

# pop() => ตัดสมาชิกตัวสุดท้ายออก
number = [1,2,3,4,5,6]
print(number)
number.pop()
print(number)

print("\n")

# clear() => ลบข้อมูลใน list ออกทั้งหมด เเต่ยังเหลือ list เปล่าๆอยู่ (ไม่เหมือน del)
actress = ["eva green","kate blenchat","julie"]
print(actress)
actress.clear()
print(actress)

print("\n")

# del nameOfList[index] => delete by use index
girls = ["Anna","Jew","Nutcha","Fern"]
print(girls)
del girls[3]
print(girls)

print("---------------------------------")

# del สามารถ ลบ list ทิ้งได้เลย(clear หน่วยความจำ)

boys = ["napat","guy","pluem","tarzan"]
print(boys)
del boys
print(boys) # it will show list boys is not defined
