# access data in list
'''
                 Length = 5
        
           | a | b | c | d | e |
index-->     0   1   2   3   4
            -5  -4  -3  -2  -1  <-- negative index

'''

# Ex.เข้าถึงข้อมูลเเบบกำหนดช่วง

all=[10,"Mr.Egg",True,3.14,-10]

print(all[1:4])   # print list all index ที่ 1,2 เเละ 3
print(all[-3:-1]) # print list all index ที่ -2 เเละ -1
print(all[1:])    # print list all index ที่ 1 ไปถึงตัวสุดท้าย
print(all[-1:])   # print เเค่ -10 เท่านั้น
print(all[-5:])   # print ตั้งเเต่ index ที่ -5 ถึง -1 