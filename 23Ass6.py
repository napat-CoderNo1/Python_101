# สร้างขอบตาราง

'''
input = 4
output
xxxx
x  x
x  x
xxxx

'''
line = int(input("Enter number: "))

for countLine in range(line):
    for countInRow in range(line):
        if countLine==0 or countInRow==0:
            print("x",end='')
        elif countLine==line-1 or countInRow==line-1:
            print("x",end='') 
        else:
            print(" ",end='')
    print(" ")