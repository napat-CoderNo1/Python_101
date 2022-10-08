# difference
fruitA = {"banana", "star gooseberry", "lime", "apple", "durian"}
fruitB = {"apple", "durian", "strawberry", "kiwi", "mango"}
fruitC = fruitA.difference(fruitB) # print ตัวที่มี่เฉพาะใน fruitA (เหมือนกับ A-B ในเรื่องเซต)
print("fruitC = ", fruitC)

print("\n")

# difference_update => ต่างจาก dofference ตรงที่ ไม่ต้องสร้างเซต C ขึ้นมาใหม่
boy = {"napat", "ball", "bird"}
print("old boy = ", boy)
boyNgirl = {"jew", "sense", "fone", "bird", "ball"}
boy.difference_update(boyNgirl)
print("new boy = ", boy)