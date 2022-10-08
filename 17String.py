''' การเข้าถึงตัวอักษรใน string '''

name1 = "Napat Moonpinij"

print(name1)      # print => Napat Moonpinij

print(name1[0])   # print => N

print(name1[5])   # print => ช่องว่าง(ระหว่าง t กับ M)

print(name1[0:3]) # print ตั้งเเต่ index ที่ 0-2 => Nap

print(name1[:3])  # print ตั้งเเต่ index ที่ 0-2 => Nap

print(name1[2:9]) # print ตั้งเเต่ index ที่ 2-8 => pat Moo

print(name1[-3])  # print index ที่ 2 นับจากด้านหลัง => n (ที่ต้องลดจากใน [] ไป 1 เพราะนับจากด้านหลัง index ไม่ได้เริ่มที่ 0)

print(name1[-2])  # print index ที่ 1 นับจากด้านหลัง => i

print(name1[-1])  # print index ที่ 0 นับจากด้านหลัง => j

''' length of string '''
# len()
# strip()

name2 = "napat"
name3 = "  napat  "

print(len(name2)) # len() function => print length of string => 5
print(len(name3)) # นับช่องว่าเป็น index ด้วย => print length of string => 9

print(len(name3.strip()))  # strip() function => ลบช่องว่าง "ทั้งหมด" ออก => print length of string => 5

print(len(name3.lstrip())) # lstrip() function => ลบช่องว่างทาง "ด้านซ้าย" ออก => print length of string => 7
print(len(name3.rstrip())) # rstrip() function => ลบช่องว่างทาง "ด้านขวา" ออก => print length of string => 7

''' upper case to lower case '''
# upper()
# lower()
# capitalize()

name4 = "KoNg"
print(name4.upper()) # print "KONG"
print(name4.lower()) # print "kong"

name5 = "napat moonpinij"
# อยากให้เฉพาะตัวเเรกสุดเป็นตัวพิมพ์ใหญ่
print(name5.capitalize())


''' replace word by word '''
# replace()

name6 = "anna nattika anna naroke"
print(name6.replace("anna","napat")) # เเทนที่ anna ด้วย napat

name7 = "anna nattika anna narak"
print(name7.replace("anna","na",1)) # ถ้าต้องการเปลื่ยน anna ตัวเเรกเท่านั้นตัวหลังไม่เปลื่ยน


''' check word '''

# เช็คว่ามีคำนั้นในประโยคหรือไม่ ถ้ามี return => true ไม่มี return => false

name8 = "I want to play game"  # เช็คว่ามีคำว่า game หรือไม่มี

x1 = "game" in name8
print(x1)

x2 = "anna" in name8
print(x2)