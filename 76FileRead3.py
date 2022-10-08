try:
    fr = open("score.txt","r",encoding="utf-8")
    line = fr.readlines() # อ่านทีละบรรทัด
    for x in line:
        print("=>",x)
    fr.close()
except:
    print("file not found")