boys  = {"napat", "ball", "pleum"}
girls = {"suzy", "jew", "baitong","ball"}

boysForTestUpdate  = {"napat", "ball", "pleum"}
girlsForTest = {"suzy", "jew", "baitong","ball"}

# update() # ต่างกับ union ตรงที่ ไม่ต้องสร้าง set เพิ่ม
print("# update")
print("boysForTestUpdate before update girls = ", boysForTestUpdate)
boysForTestUpdate.update(girls)
print("boysForTestUpdate after update girls = ", boysForTestUpdate)
print("\n")

# union
print("# union")
boyUgirl = boys.union(girls) # สร้าง set boyUgirl ขึ้นมาใหม่
print("boys union girls = ", boyUgirl) # ball ซ้ำกัน print เเค่ตัวเดียว
print("\n")

# intersection
print("# intersection")
boyIntersecGirl = boys.intersection(girls)
print("boys intersection girls = ", boyIntersecGirl)
print("\n")

# intersection_update
print("# intersection_update")
print("old girlsForTest = ", girlsForTest)
girlsForTest.intersection_update(boys)
print("new girlsForTest = ", girlsForTest)