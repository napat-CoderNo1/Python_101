''' Concatinate (ต่อ string โดยใช้ + ) '''

fname = "Napat "
lname = "Moonpinij "
age = "20"
salary = 500.9875

fullname = fname + lname + age
print(fullname)

print("FirstName : " + fname + "LastName : " + lname + "Ages : " + age)

#--------------------------------------------------------------------------------------------------

''' จัดรูปเเบบการเเสดงผล '''
# format()
                                                                          
# ในช่อง {} คือจุดที่เราจะใส่ตัวเเปรลงไป
# {4:.2f} คือเเสดงทศนิยมเเค่ 2 ตำเเหน่ง

text1 = "FirstName : {0}LastName : {1}Ages : {2} Career : {3} Salary : {4:.2f}" 

#             index  0     1    2       3          4   
print(text1.format(fname,lname,age,"Programmer",salary))

#-------------------------------------------------------------------------------------------------

''' นับจำนวนคำในประโยค '''
# count()

#                                    1                     2
fruit = "I go to Buy fruit such as apple orange grape pieapple at market"

# find number of word "apple" in above sentence
print(fruit.count("apple"))

#--------------------------------------------------------------------------------------------------

''' เช็คคำขึ้นต้น '''
# startswitch()
# endswitch()

text2 = "Mr. napat lhor mak mak"
print(text2.startswith("Mr."))   # print => True
print(text2.startswith("napat")) # print => False
print(text2.endswith("mak"))     # print => True
print(text2.endswith("ak"))      # print => True

if text2.startswith("Mr.") :
    print("Male")
else :
    print("Female")