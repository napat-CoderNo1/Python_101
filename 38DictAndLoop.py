gun = {"m4a1":20, "m16":100, "bazuka":"boom"}

# print only key
for i in gun:
    print(i)
for i in gun.keys():
    print(i)

print("\n")

# if you want to show value
for i in gun.values():
    print(i)

print("\n")

# if you want to show both key and value
for k, v in gun.items():
    print("key = ", k, "value = ", v)