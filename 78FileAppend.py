# ถ้าอ่านเสร็จเเล้วอยากเพิ่มข้อมูลอีกล่ะ
try:
    fr = open("score.txt","r",encoding="utf-8")
    line = fr.readlines() # อ่านทีละบรรทัด
    for x in line:
        print("=>",x)

    fw = open("score.txt","a",encoding="utf-8") # เปลื่ยนโหมดเป็นโหมด a จะเป็นการเพิ่มข้อมูลต่อท้าย
    fw.write("Fuck") 
    
    fr.close()
    fw.close()
except:
    print("file not found")