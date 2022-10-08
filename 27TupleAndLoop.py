tup = (1, 2, 3.3, "Napat", True)

# Ex1 => Print all data in tuple
for i in tup:
    print(i, end=' ')
    print(type(i))

print("\n")
print("------------------------------")

# Ex2 => use len() ...> same len() in List
print("len(tup) = ", len(tup))
for i in range(len(tup)):
    print(i, end='  ')
