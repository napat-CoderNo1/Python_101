# ตัวเลขขั้นบันได
'''
Ex. input = 3
output
1
12
123

row    = เเถว
line = บรรทัด

'''
line = int(input("Enter Number: "))
row=1
i=0 # ตัวนับภายในเเถว (เเนวนอน)
j=0 # ตัวนับบรรทัด (เเนวตั้ง)

for j in range(j,line):
    i=0
    for i in range(i,row):
        print(i+1,end=" ")
        i=i+1
    print("\n")
    row = row+1