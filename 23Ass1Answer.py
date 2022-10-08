start,stop = 1,5 # start=1 , stop=5
sum=0

while (start<=stop):
    number = int(input("Enter Number: "))
    sum = sum+number
    start = start+1

print("Summation = ",sum)