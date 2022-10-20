# เเลกเงิน
# Ex
# 1000 => 500 2 ใบ
# 1800 => 1000 1 ใบ, 500 1 ใบ, 100 3 ใบ
# 1550 => 1000 1 ใบ, 500 1 ใบ, 50 1 ใบ


amount = int(input("Enter amount : "))

a = int(amount/1000)
amount = amount - (a*1000)
print("เเบงค์ 1000",a,"ใบ")
    
b = int(amount/100)
if b < 5 :
    print("เเบงค์ 100 ",b,"ใบ")
else :
    print("เเบงค์ 500 1 ใบ / เเบงค์ 100 ",b-5,"ใบ")
amount = amount - (b*100)

c = int(amount/10)
if c >= 5 :
    print("เเบงค์ 50 1 ใบ")
    if (c-5)%2 == 0 :
        print("เเบงค์ 20",int((c-5)/2),"ใบ")
    elif c == 8 :
        print("เเบงค์ 20 1 ใบ / เหรียญ 10 1 เหรียญ")
    elif c == 6 :
        print("เหรียญ 10 1 เหรียญ")
else :
    if c%2 == 0 :
        print("เเบงค์ 20",int(c/2),"ใบ")
    elif c == 3 :
        print("เเบงค์ 20 1 ใบ / เหรียญ 10 1 เหรียญ")
    elif c == 1 :
        print("เหรียญ 10 1 เหรียญ")

amount = amount - (c*10)

d = amount
if d >= 5 :
    print("เหรียญ 5 บาท 1 เหรียญ / เหรียญ 1 บาท",d-5,"เหรียญ")
else :
    print("เหรียญ 1 บาท ",d," เหรียญ") 

# other version
# money = int(input("Enter money: "))
# temp = 0

# if money >= 1000:
#     temp = money//1000
#     print("1000("+str(temp)+")", end=', ')
#     money = money%1000

# if money >= 500:
#     print("500(1)", end=', ')
#     money = money%500

# if money < 500:
#     if money >= 100:
#         temp = money//100
#         print("100("+str(temp)+")", end=', ')
#         money = money%100

# if money < 100:
#     if money >= 50:
#         print("50(1)", end=', ')
#         money = money%50

# if money < 50:
#     if money>=20:
#         temp = money//20
#         print("20("+str(temp)+")", end=', ')
#         money = money%20

# if money < 20:
#     if money>=10:
#         print("10(1)", end=', ')
#         money = money%10

# if money < 10:
#     if money>=5:
#         print("5(1)", end=', ')
#         money = money%5
#         if money!=0:
#             print("1("+str(money)+")")
#     elif money!=0:
#         print("1("+str(money)+")")