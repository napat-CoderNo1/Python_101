# args ทำให้ใส่ Arguments กี่ตัวก็ได้
# kwargs ทำให้มี Parameter กี่ตัวก็ได้

# function

def displayData(**kwargs): # ข้อมูลที่ส่งเข้ามาใน kwargs จะเป็น Dictionary
    print(kwargs)
    print(kwargs["fname"])

# main program

displayData(fname = "Bae", lanme = "Suzy", age = "30")
displayData(fname = "Park", lname = "Minyong")
displayData(fname = "Toni", lname = "Rakkan", age = "35", job = "actor")