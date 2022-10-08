# function

def displayData(fname, lname, city):
    print("name = ", fname)
    print("lastname = ", lname)
    print("city = ", city)

# main program

displayData("Napat", "Moonpinij", "Samutprakarn")
print("\n")

# เเล้วถ้าใส่จังหวัดก่อนนามสกุลล่ะ ค่าที่เเสดงออกมาก็จะเพี้ยนไป

displayData("Napat", "Samutprakarn", "Moonpinij")
print("\n")

# เเก้โดย keyword arguments

displayData(city="Samutprakarn", fname="Napat", lname="Moonpinij")
