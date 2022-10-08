# delete only data from tup
tup1 = (1, 2, 3.3, "Napat", True)
print("old tup1 = ", tup1)
'''
delete 3.3 from tup1

wrong solution1
del tup[2] => Error
'''
# convert tuple to list
# ann then you can use pop(), remove(), del()
lis = list(tup1)
lis.remove(3.3)

# update to tup1
tup1 = tuple(lis)
print("new tup1 = ", tup1)

print("\n")

# delete tup from memory
tup2 = (1, 2, 3.3, "Napat", True)
print("tup2 = ", tup2) # can print tup
del tup2    # delete tup from memory
print(tup2) # cannot print tup => Error