# Ass1 รับข้อมูลตัวเลขเข้ามาใน list เเล้ว เรียงลำดับ
# ความรู้ใหม่ sort(),reverse()

number = []

print(number)

count = int(input("Enter count of number: "))

for i in range(0,count,1):
    x = int(input("Enter number: "))
    number.append(x)

print("before sort: ",number)

# sort() => เรียงค่าตัวเลขใน list จากน้อยไปมาก
number.sort()
print("after sort : ",number)

# reverse() => เรียงค่าตัวเลขใน list จากมากไปน้อย
number.reverse()
print("after reverse : ",number)
