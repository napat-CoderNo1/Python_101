''' For Loop '''

# structure
''' for i in range(start, stop, step) '''

# print 0,1,2
for i in range(3) :
    print(i)

print("--------------------------------------------")

# print "Hello World" 5 times
for i in range(5) :
    print("รอบที่ ",i+1," Hello World")

print("--------------------------------------------")

# print "Hello World" only 3 times => round 2,3,4
for i in range(2,5) :
    print("Round ",i,"Hello World")

print("--------------------------------------------")

# print "Hello World" only 5 times => round 2,4,6,8,10
for i in range(2,12,2) :
    print("round ",i," Hello World")

print("--------------------------------------------")

# print "Hello World" only 6 times => round 0,2,4,6,8,10
for i in range(0,12,2) :
    print("round ",i," Hello World")

print("--------------------------------------------")

# + ตัวเลขตั้งเเต่ 0-4
sum = 0
for i in range(5) :
    sum = sum+i
    print("round ",i," sum = ",sum)

print("--------------------------------------------")

# ค่า start,stop,step ติดลบ ได้ 
# print round => -10,-9,-8,...,2,3,4
for i in range(-10,5,1) :
    print("round ",i)