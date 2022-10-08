try:
    fr = open("score.txt","r",encoding="utf-8")
    line = fr.readline() # อ่านทีละตัวอักษร เเละ เฉพาะ บรรทัดเเรกด้วย จบที่ justin
    for x in line:
        print(x)
    fr.close()
except:
    print("file not found")