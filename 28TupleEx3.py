# reversed tuple

# first solution
x = (100, 20, 30, 15, 10, 5, 500)
print("old x = ", x)
x = x[::-1]
print("new x = ", x)

print("\n")

# second solution
y = (12, 3, "napat", True, 3.3)
print("old y = ", y)
y = reversed(y)
y = tuple(y) # ถ้าไม่มีบรรทัดนี้จะเเสดงไม่ได้
print("new y = ", y)

# Tip reversed and string
z = "bae suzy" # string
print("old z = ", z)
z = tuple(reversed(z))
print("new z = ", z)