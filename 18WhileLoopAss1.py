# find a sum of number and then find an average

x = int(input("Enter Number : "))
count = 1
sum = 0

while count <= x :
    sum = sum + count 
    count = count + 1

print("sum = ",sum)
print("average = ",sum/x)