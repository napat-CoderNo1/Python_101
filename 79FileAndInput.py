try:
    fw = open("input.txt","a",encoding="utf-8")
    name = input("Enter text : ")
    fw.writelines(name+"\n")
    fw.close()
except FileNotFoundError :
    print("File not found")
