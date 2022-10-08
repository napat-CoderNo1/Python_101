# Compound Assignment
# +=, -=, *=, /=, //=, **=, %=

x1 = 10
print("x1 before add value = ", x1)
# use "x1+=5" same result
x1 = x1+5
print("x1 after add value = ", x1)

print("\n")

x2 = 10
print("x2 before minus value = ", x2)
x2 -= 5
print("x2 after minus value = ", x2)

print("\n")

x3 = 10
print("x3 before multiply by number = ", x3)
x3 *= 3
print("x3 after multiply by number = ", x3)

print("\n")

x4 = 10
print("x4 before ยกกำลัง = ", x4)
x4 **= 3 # x = x**3
print("x4 after ยกกำลัง = ", x4)

print("\n")

x5 = 10
print("x5 ก่อนหารเอาเศษ  = ", x5)
x5 //= 4
print("x5 หลังหารเอาเศษ = ", x5)

print("\n")

x6 = 10
print("x5 ก่อนหารเอาเศษ  = ", x6)
x6 %= 4
print("x5 หลังหารเอาเศษ = ", x6)

# //= ใช้เหมือนกับ %=