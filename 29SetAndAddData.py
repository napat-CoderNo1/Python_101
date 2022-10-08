# เพิ่มข้อมูลทีละตัว
# add()
fruit = {"mango", "grape", "watermelon"}
print("old fruit = ", fruit)
fruit.add("durian")
print("new fruit = ", fruit)

print("\n")

# เพิ่มทีละหลายตัว
# สร้าง list ขึ้นมา เเล้ว update()
gun = {"m16", "aka47", "m4a1"}
print("old gun = ", gun)
lis = ["uzy", "galing", "bazuka"]
gun.update(lis)
# เขียนรวบไปเลยเเบบนี้  gun.update(["uzy", "galing", "bazuka"]) ก็ได้ โดยไม่ต้องสร้าง lis ขึ้นมา
print("new gun = ", gun)
