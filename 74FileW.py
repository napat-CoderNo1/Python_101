try:
    # fw = open("score.txt", "x", encoding="utf-8") # พอกด run จะได้ file score.txt เปล่าๆมา
    fw = open("score.txt", "w", encoding="utf-8") # พอเป็น w จะสามารถใส่ข้อมูลได้
    fw.write("Hello World") # ใน file score.txt จากที่เป็นไฟล์เปล่าๆ ก็จะมี text เขียนว่า Hello World
    fw.write("Hello Girls") # เขียน Hello Girls ต่อในบรรทัดเดียวกัน
    fw.writelines("Hello Boys") # เขียนเเบบนี้ก็ยังจะไม่ขึ้นบรรทัดใหม่
    fw.write("Hello Justin\n")
    fw.write("Hello Halie")
    fw.close() # ทุกครั้งที่ดำเนินการเกี่ยวกับ file ต้องมีการปิด file
except FileNotFoundError :
    print("file not found")