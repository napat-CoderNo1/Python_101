z = "20"
print("first z type = " + str(type(z)))

float(z)
print(type(z)) # type of z still string

z = float(z)
print(type(z)) # type of z change to float already