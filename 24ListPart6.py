# การเพิ่มข้อมูลใน List

# append() => นำมาสมาชิกใหม่มา "ต่อท้าย"
fruit = ["Apple","Pie Apple","Watermelon","Givi"]
print("Before add: ",fruit)
fruit.append("Grape")
print("After add: ",fruit)

print("\n")

# insert(index,สมาชิกใหม่) => เเทรกสมาชิกใหม่เข้ามาก่อนหน้า index ตัวที่กำหนด
cars = ["camelo","mustang","Lambo","bugati"]
print(cars)
cars.insert(0,"honda")
print(cars)
