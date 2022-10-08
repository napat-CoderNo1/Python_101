import random

ATM_PASSWORD = "k0"
result = ""

while result != ATM_PASSWORD:
    result = ""
    for i in range(len(ATM_PASSWORD)):
        list_number = random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
        result="".join(list_number)+str(result)
        print("SEARCH = ", result)
print("Crack Password Is ", result)