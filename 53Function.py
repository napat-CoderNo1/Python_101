# function เรียก function

def equal(x,y,z):
    max1 = compareMax(x,y) # เรียกใช้ function compareMax ใน function equal อีกที
    max2 = compareMax(max1,z)
    return max2

def equal2(x,y,z):
    return compareMax(compareMax(x,y), z) # เขียนเเบบนี้จะเป็นการย่อ equal

def compareMax(x,y):
    if x>y:
        return x
    else:
        return y

max = compareMax(10,20)
print("max number = ", max)

print("\n")

maxx = equal(10,5,7)
print("max of 3 number = ", maxx)