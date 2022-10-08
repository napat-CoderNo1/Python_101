# ตัวเลขขั้นบันได เเบบอีกวิธี
# for i in range(start,stop,step)
line = int(input("Enter Number: ")) # ใส่เลขเพื่อกำหนดให้รู้ว่าจะมีกี่บรรทัด (เเนวตั้ง)
row = 1 # เริ่มที่เเถว 1
for i in range(0,line,1): # Loop สำหรับนับบรรทัด
    for j in range(0,row,1): # Loop สำหรับนับจำนวนตัวในเเต่ละเเถว
        print(j+1,end='')
    row = row+1 # เพิ่มค่า row เพื่อบอกว่าเป็นเเถวต่อไปเเล้วนะ
    print("\n") # newline