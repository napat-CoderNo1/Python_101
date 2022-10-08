# you can use "Else" with "While Loop"
i=1
while i<=10:
    print("Round: ",i)
    i=i+1
else:
    print("End Program")

print("------------------------------------")

# Break
i3=1
while i3<=10:
    print("Round: ",i3)
    if i3==5:
        break # End Loop suddenly 
    i3=i3+1

print("End Program")

print("------------------------------------")

# Continue
i2=0
while i2<=10:
    i2=i2+1
    if i2==5:
        continue # พอ i==5 จะข้ามการทำงานบรรทัดที่ 29ไป เเล้วไปเช็คลูป while ใหม่
    print("Round: ",i2)

print("End Program")

print("------------------------------------")

# EX. ข้ามเมื่อ i เป็นเลขคี่

i4=0
while i4<=10:
    i4=i4+1
    if (i4%2 != 0):
        continue
    print("Round: ",i4)

print("End Program")