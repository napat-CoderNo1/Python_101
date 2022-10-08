# open(name of file , mode , encode)
# ชื่อไฟล์ พิมพ์ใหญ่ พิมพ์เล็กได้หมด ขอเเค่ชื่อเหมือนพอ
# mode มีหลายโหมด อ่าน r , เขียน w , append a ฯลฯ


fr = open("student.txt", "r")
print(fr.read()) # print text ทั้งหมด
# print(fr.read(5)) # อ่านเเค่ 5 ตัวอักษร

print("\n")

# ถ้าใน text file มี ภาษาไทย ต้องมีการ encoding เพื่อให้ print ออกมาได้
fr2 = open("student.txt", "r", encoding="utf-8")
print(fr2.read())