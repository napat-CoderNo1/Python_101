fa = open("Point.txt","a",encoding="utf-8")
for i in range(5):
    studentID = input("Enter student ID : ")
    point = input("Enter score : ")
    fa.write("stdID : "+studentID+" score : "+point+"\n")
fa.close()

fr = open("Point.txt","r",encoding="utf-8")
fw = open("Grade.txt","a",encoding="utf-8")

for line in fr.readlines():
    score = int(line[-4:].strip())
    stdId = line[:10]
    grade = None

    if score >= 80:
        grade = 'A'
    elif score <= 79 and score > 69 :
        grade = 'B'
    elif score <= 69 and score > 59 :
        grade = 'C'
    elif score <= 59 and score > 49 :
        grade = 'D'
    elif score <= 49 :
        grade = 'F'

    fw.writelines(stdId+" , "+"score : "+str(score)+" , Grade : "+grade+"\n")
fw.close()
fr.close()