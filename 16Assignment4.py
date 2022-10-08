weight = int(input("Enter your weight (kg) : "))
hight = int(input("Enter your hight (cm) : "))
hight = hight/100

BMI = weight/(hight**2)

print("BMI : ",BMI)

if BMI < 18.5 :
    print("ต่ำกว่าเกณฑ์")
elif BMI >= 18.5 and BMI <= 22.9 :
    print("สมส่วน")
elif BMI >= 23.0 and BMI <= 24.9 :
    print("น้ำหนักเกิน")
elif BMI >= 25.0 and BMI <= 29.9 :
    print("โรคอ้วน ระดับ 1")
else :
    print("โรคอ้วนอันตราย")