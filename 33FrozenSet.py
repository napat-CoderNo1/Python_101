# set เเบบธรรมดา เพิ่ม, ลด ข้อมูลได้
fruit = set(["mango", "lime", "apple", "orange"])
print("old fruit = ", fruit)
fruit.add("durian")
print("new fruit = ", fruit)
fruit.discard("mango")
print("new fruit2 = ", fruit)

print("\n")

# frozen set
gun = frozenset(["m4a1", "m16", "uzy"])
print("old gun = ", gun)
gun.add("bazuka")
print("new gun = ", gun) # error => frozen set can't add or discard data