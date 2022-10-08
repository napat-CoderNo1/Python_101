# สลับค่าระหว่าง tuple x --> tuple y
x = (50,60)
y = (88,99)

print("old x = ", x)
print("old y = ", y)

x, y = y, x

print("new x = ", x)
print("new y = ", y)