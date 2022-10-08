# รับค่าตัวเลขเข้ามาใน List เเล้ว จำเเนกกลุ่มเลขคู่เเละเลขคี่ืี
numbers = []
print(numbers)
count = int(input("Enter count: "))
i = 0
while i<count:
    x = int(input("Enter number: "))
    numbers.append(x)
    i = i+1
print(numbers)
odd = []
even = []
for j in range(0,len(numbers),1):
    if numbers[j] % 2 == 0:
        even.append(numbers[j])
    else:
        odd.append(numbers[j])
print("odd = ",odd)
print("even = ",even)