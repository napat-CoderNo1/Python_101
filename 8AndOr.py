# AND
# OR
# NOT

# results => True/False

x = (10>5)       # x == boolean => True
print(type(x))   # x == boolean
print(x)         # x == True

y = (10==5)      # y == boolean => false
print(type(y))   # y == boolean 
print(y)         # y == false

print("\n")

# z1 = (10>5) and (10==5)
# z1 = True and False
# z1 = False
z1 = x and y
print("z1 = ", z1)

# z2 = (10>5) or (10==5)
# z2 = True or False
# z2 = True
z2 = x or y
print("z2 = ", z2)
print("not z2 = " , not z2)