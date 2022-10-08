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