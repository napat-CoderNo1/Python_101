# Program calculate BMI
# BMI = weight(kg) / hight(meters) * hight(meters)

# input
weight = float(input("Enter your weights(kg) : "))
hight = float(input("Enter your hights(cm) : "))

# process
hight_m = hight/100
BMI = weight/(hight_m*hight_m)

# output
print("your BMI : ", BMI)