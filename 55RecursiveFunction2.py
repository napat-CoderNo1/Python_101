# recursive function หาผลรวมตัวเลข 3 ถึง 1

def summation(number):
    if number == 1:
        return number
    else:
        return number+summation(number-1)

x = summation(3)
print(x)

'''
first step:
number == 3
return 3+summation(2)

step 2:
คิดที่ summation(2)
number == 2
return 2 + summation(1)

step 3:
คิดที่ summation(1)
number == 1
return 1

จบ recursive function

สรุป 3 + summation(2)      => summation(2) return : 2+summation(1)
      + 2 + summation(1)  => summation(1) return : 1
          + 1

=> 3+2+1 = 6 
'''