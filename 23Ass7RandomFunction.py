# เกมทายลูกเต๋า
'''
1.random 1-6
2.player เดา 
3.เดาถูกได้ขึ้นว่าถูกเดาผิดขึ้นว่าผิด

'''
# random number of dice
import random # import class random to use
myRandom = random.randrange(1,7) # random 1-6

while True:
    number=int(input("Enter your answer: "))
    if number == myRandom:
        print("Correct")
        break 
    else:
        print("Mother fucker")