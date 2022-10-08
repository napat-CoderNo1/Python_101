import math

# square root
y1 = math.sqrt(64) # หารากที่สอง
print(y1)

# ปัดขึ้น/ปัดลง
score1 = math.floor(80.7) # ปัดลง
print(score1)
score2 = math.ceil(80.3) # ปัดขึ้น
print(score2)

# ค่า PI
print("ค่า PI = ", math.pi) # ค่า PI

# ค่าทางตรีโกณมิติ
m1 = math.sin(30.00) # ค่าที่ได้ออกมาจะไม่เป็น 1/2 เพราะ 90 ที่ใส่ไป เป็น 90 องศา ต้องทำให้เป็น radians
print(m1)
m2 = math.radians(30)  # degree => radians
print(math.sin(m2)) # จะได้ 0.499999 ประมาณ 0.5 หรือ 1/2 นั่นเอง


print("\n")

# built in function => function ที่ไม่ต้อง import เข้ามาใช้งาน

x1 = min(3,4,5,-10,100) # min() function หาตัวเลขน้อยสุด
print(x1)

x2 = max(-10,-5,-6,100) # max() function หาตัวเลขมากสุด
print(x2)

x3 = abs(-50) # abs() หา absolute
print(x3)

x4 = pow(5,2) # หาเลขยกกำลัง => 5ยกกำลัง2
print(x4)