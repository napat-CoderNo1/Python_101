''' Temperature unit converter '''

# C = (F-32) * (5/9)
# F = [C*(9/5)] + 32

print("Ex. 45F means 45 fahrenheit")
temp = input("Enter temperature degree and unit : ")

temperatureInFahrenheit = ((int(temp[0:len(temp)-1]))*(9/5))+32
temperatureInCelcius = (int(temp[0:len(temp)-1])-32)*(5/9)

x1 = "C" in temp
x2 = "F" in temp

if x1 :
    print("Temperature in fahrenheit is : ",temperatureInFahrenheit,"F")
elif x2 :
    print("Temperature in Celcius is : ",temperatureInCelcius,"C")