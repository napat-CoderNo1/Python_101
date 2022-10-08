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