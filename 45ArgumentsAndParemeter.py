# function
def myData1(a, b, c): # parameter ก็คือตัวเเปรที่รับค่าข้อมูลที่ Arguments ส่งเข้ามา (a, b, c)
    print("first name: ", a, "last name : ", b ,"age : ", c)

def sum(a,b):
    print(a+b)

# main program

# Arguments send value to function (fname, lastN, age)
fname = "Napat"      
lastN = "Moonpinij"  
age   = 19    

myData1(fname, lastN, age)
sum(5,9) # 5,9 is an Arguments