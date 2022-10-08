# tuple not have function sort()
# tup1.sort() => Error
# วิธีที่ถูก คือ เเปลงเป็น list เเล้วค่อย sort
tup1 = (99, 98, 96, 97, 100)
print("tup1 before sort = ", tup1)
lis = list(tup1)
lis.sort() # min --> max
tup1 = tuple(lis)
print("tup1 after sort = ", tup1)