# Add Data to tuple
tup = (1, 2, 3.3, "Napat", True)
newData = "Anna"
print("tup before add data = ", tup)

'''
Wrong Solution
cannot do this => tuple + string
tup = tup+newData
print(tup) => Error
'''

# Solution One (not Best)
# Change newData = "Anna" (string) => tuple
newData = ("Anna",)
tup = tup+newData # tuple+tuple => this call join
print("tup after add data  = ", tup)
