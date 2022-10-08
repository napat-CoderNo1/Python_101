# if you want to change 20:False => 20:True
colors = {"red":True, "orange":19.56, "yellow":'V', 20:False, "purple":20}
print("old colors = ", colors)
colors[20] = True
print("new colors = ", colors)
print("\n")

# add new data to dict
gun = {"m4a1":20, "m16":100, "bazuka":"boom"}
print("old gun = ", gun)
gun.update({"uzy":True}) # function update() ถ้า key ไม่ซ้ำจะเป็นการเพิ่มข้อมูล เเต่ถ้า key ซ้ำ จะเป็นการเเก้ไขข้อมูลเเทน
gun.update({"m4a1":False}) # key ซ้ำ
print("new gun = ", gun)
print("\n")