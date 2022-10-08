# build square
'''
input = 4
****
****
****
****

input = 2
**
**
'''

line = int(input("Enter Number: "))

for countLine in range(0,line,1):
    for countInRow in range(0,line,1):
        print("x",end='')
    print(" ")