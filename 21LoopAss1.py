# รับค่าเเล้ว เเสดงเเม่สูตรคูณ 
n = int(input("Enter Number: "))
print("ตารางสูตรคูณเเม่ ",n)
for i in range(1,13) :
    print(n,"x",i," = ",n*i)

# เเสดงตารางสูตรคูณ เเม่ 2-4
for i in range(2,5) :
    print("ตารางสูตรคูณเเม่ ",i)
    for j in range(1,13) :
        print(i,"x",j," = ",i*j)