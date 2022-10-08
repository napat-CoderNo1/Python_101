# เวลาเรียกใช้ module สามารถตั้งชื่อเล่นให้ module ได้ จะได้ไม่ต้องพิมพ์ WeatherModule. ทุกครั้ง โดยการ as ชื่อเล่น
import MyModule.WeatherModule as W

x = W.city["Chonburi"]
print(x)

W.getWearher()
