tup = (1, 2, 3, 4, "Bae Suzy", "mango", True, 3.99) # Tuple
city = ["Bangkok", "London", "New York"]
print("old tup = ", tup)

'''
if you want to add data from List city to Tuple tup 
you should change List city to Tuple first
'''

# it's call Join
tup = tup + tuple(city)
print("new tup = ", tup)