# function

def displayData(fname, lname, city):
    print("name = ", fname)
    print("lastname = ", lname)
    print("city = ", city)

# main program

displayData(city="Bangkok", lname="Suzy", fname="Bae")

'''
ถ้าใส่ parameter ไม่ครบก็จะ error
displayData(fname="Bangkok", lname="Suzy")
'''
print("\n")

# เเก้ไขโดยการกำหนด default parameter

def displayData2(fname, lname, city="Bangkok"):
    print("name = ", fname)
    print("lastname = ", lname)
    print("city = ", city)

# Bae Suzy จะไปอยู่กรุงเทพโดยอัตโนมัต ถ้าไม่ใส่ parameter city
displayData2(fname="Bae", lname="Suzy")