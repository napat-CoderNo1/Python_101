# pop(key)
gun = {"m4a1":20, "m16":100, "bazuka":"boom"}
print("old gun = ", gun)
gun.pop("m4a1")
print("new gun = ", gun)

print("\n")

# popitem() ตัดสมาชิกตัวท้ายสุดออก
gun2 = {"m4a1":20, "m16":100, "bazuka":"boom", "uzy":23}
print("old gun2 = ", gun2)
gun2.popitem()
print("new gun2 = ", gun2)
gun2.popitem()
print("new gun2 = ", gun2)

print("\n")

# clear() ลบสมาชิกทุกตัวออกเหลือ dict ว่าง
numbers = {"num1":20, "num2":10, 20:True}
print("old numbers = ", numbers)
numbers.clear()
print("new number = ", numbers)

print("\n")

# del() เหมือนเรื่องเก่าๆคือลบทิ้งไปเลย