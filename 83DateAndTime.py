# Module Date / Time
import datetime

x = datetime.datetime.now() # current date and current time
print(x)
print(x.year)
print(x.month)
print(x.hour)
print(x.minute)

print("\n")

# กำหนดวันเวลาเอง
newX = datetime.datetime(2020,6,20,15) # yyyy,m,d,time
print(newX)

print("\n")

# รูปเเบบการเเสดงผล
print("basic = ", x)
print(x.strftime("%x")) # m/d/y สั้น
print(x.strftime("%X")) # เวลา time
print(x.strftime("%c")) # ชื่อวัน(Ex. จัน,อังคาร) เดือน วันที่ เวลา ปี
# Time
print(x.strftime("%H")) # เเสดง จำนวน ชั่วโมง เช่น หากตอนนี้เวลา 16.32 ก็จะเเสดงเเค่ 16
print(x.strftime("%M")) # เเสดงจำนวนนาที
print(x.strftime("%S")) # เเสดงจำนวนวินาที
print(x.strftime("%p")) # เเสดง AM , PM
print(x.strftime("%H : %M : %S : %p"))

print("\n")

# Date
print(x.strftime("%j")) # อยากรู้ว่าวันนี้เป็นวันลำดับที่เท่าไหร่ของปี (1-366)
print(x.strftime("%a")) # บอกว่าวันนี้วันอะไรเเบบย่อ (Mon, Wed, Fri, Sun)
print(x.strftime("%A")) # เเสดงวันเเบบเต็ม Friday
print(x.strftime("%w")) # 0=sunday , 1=monday , ....
print(x.strftime("%d")) # บอกวันที่ 16,1,5,10,31,29,...
print(x.strftime("%b")) # เเสดงเดือนเเบบย่อ
print(x.strftime("%B")) # เเสดงเดือนเเบบเต็ม

print(x.strftime("%A date %d month %B")) # ภาษาไทยไม่ได้
print(x.strftime("%d / %m / %Y"))