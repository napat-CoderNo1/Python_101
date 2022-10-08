# ยกตัวอย่างเช่นอยากเปลื่ยนข้อมูลจาก mango => apple
# เราก็จะทำการลบ mango ออกก่อน เเล้วค่อย add() เพิ่ม apple

# remove()
fruit = {"mango", "grape", "banana"}
print("old fruit = ", fruit)
fruit.remove("mango")
print("new fruit = ", fruit)

print("\n")

# discard() ลบเหมือนกันเเต่จะไม่เกิด error เมื่อลบตัวที่ไม่มีใน set
cars = {"mustang", "lambo", "honda"}
print("old cars = ", cars)
cars.discard("bm") # ลบตัวที่ไม่มีใน set ไม่เกิด error เเต่ถ้าเป็น remove จะ error
print("new cars = ", cars)

print("\n")

# clear()
girls = {"anna", "jew", "suzy", "perth"}
print("old girls = ", girls)
girls.clear()
print("new girls = ", girls)

# del จะเป็นการลบออกจาก memory เหมือนใน list