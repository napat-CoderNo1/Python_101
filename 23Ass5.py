# ตารางหมากฮอส
'''
Ex. input = 4
output
xoxo
xoxo
xoxo
xoxo
'''

line = int(input("Enter Number: "))

for countLine in range(line):
    for countInRow in range(line):
        if countLine%2==0:
            if countInRow%2==0:
                print("x",end='')
            else:
                print("o",end='')
        else:
            if countInRow%2==0:
                print("o",end='')
            else:
                print("x",end='')
    print(" ")