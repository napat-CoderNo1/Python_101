def randomNumber(x):
    if len(x)<3:
        return # ไม่ return อะไรออกมา เเละจบการทำงานใน function เลย
    if x == "100":
        print("congrat!!")
        return 1000
    else:
        print("bad!!!")
        return 0

money = randomNumber("100")
print("reward = ", money)