# หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่

# ทำเอง (correct)
def checkString(message):
    big = 0
    small = 0
    for i in message:
        if i.isupper():
            big = big+1
        else:
            small = small+1
    print("Upper case = ", big, ", Lower case = ", small)

checkString("ABcDefg")

print("\n")

# เฉลย

def checkStr(mess):
    result = {"UPPER":0,"LOWER":0}
    for c in mess:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWER"]+=1
        else:
            pass
    return result

x = checkStr("ABcDef")
print(x)