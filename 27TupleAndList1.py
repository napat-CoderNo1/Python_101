tup = (1, 2, 3, 4, "Bae Suzy", "mango", True, 3.99) # Tuple
print("old tup = ", tup)

# Build new List and copy data from tup(Tuple)
lis = list(tup)
print("lis = ", lis)

# Change data in lis (List)
lis[0] = "Napat" # change 1 to Napat

# update data to tup(Tuple)
tup = tuple(lis)
print("new tup = ", tup)