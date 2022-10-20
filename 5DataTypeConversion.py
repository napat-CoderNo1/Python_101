x = 10
y = 3.14
z = "20"

print(type(x))
print(type(y))
print(type(z))

# บวกเลข
result1 = x+y  # int + float = float
print(result1) # 10+3.14 = 13.14
print(type(result1))

'''
result2 = x+z  # int + string
print(result2) # error because ( int + string  <-- cannot )
'''

# convert

# int(z)    string => int
# str(x)    int    => string
# float(z)  string => float
# str(y)    float  => string
# float(x)  int    => float
# int(y)    float  => int

# int(z) string => int
result3 = x + int(z) # 10 + 20 = 30
print(result3)

# str(x) int => string
result4 = str(x) + z # "10" + "20" = "1020"
print(result4)

# float(z) string => float
print(float(z))

# str(y) float => string
print(type(str(y)))