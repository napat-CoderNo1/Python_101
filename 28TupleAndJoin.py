# change tuple to string
character = ('A', 'C', 'B', 'D') # tuple
print("type character = ", type(character))

print("\n")

name = "".join(character)
print("name = ", name) # print "ACBD"
print("type name = ", type(name)) # string