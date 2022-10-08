# ถ้าอ่านเสร็จเเล้วอยากเพิ่มข้อมูลอีกล่ะ
try:
    fr = open("score.txt","r",encoding="utf-8")
    line = fr.readlines() # อ่านทีละบรรทัด
    for x in line:
        print("=>",x)

    fw = open("score.txt","w",encoding="utf-8")
    fw.write("Fuck") # ทำเเบบนี้จะเป็นการพิมพ์ Fuck ทับข้อมูลเก่าไปเลย ถ้าอยากเพิ่มล่ะ ดูที่ 78
    
    fr.close()
    fw.close()
except:
    print("file not found")