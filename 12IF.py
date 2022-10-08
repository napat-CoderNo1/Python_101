#--------------------- PART 1 IF -----------------------
'''
if boolean expression:
    statement

'''

age1 = int(input("Enter your ages1 : "))

if age1 >= 15:
    print("Title is Mrs./Mr.")
    print("End Program")

print("This isn't affected by expression in if")

print("\n")

#------------------ PART 2 IF-ELSE ---------------------

'''
if true :
    do sth
else :
    do sth
'''

age2 = int(input("Enter your ages2 : "))

if age2 >= 15:
    print("Title is Mrs./Mr.")
    print("End Program")
else :
    print("Title is Boy/Lady")
    print("End Program")

print("\n")

#------------------- PART 3 ELSE-IF ----------------------

''' elif '''

# 0-17  => Kid
# 18-29 => Teen
# 30-49 => Adult
# 50+   => Old

age3 = int(input("Enter your ages3 : "))

if age3 >= 0 and age3 < 18:
    print("Kid")
elif age3 >= 18 and age3 < 30:
    print("Teen")
elif age3 >= 30 and age3 < 50:
    print("Adult")
else:
    print("Old")