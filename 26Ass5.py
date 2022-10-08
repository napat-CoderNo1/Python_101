# การค้นหาเเละนับจำนวนตัวอักษรใน List

message = ["aa","aaaab","acvb","acca","rca"]

for i in range(0,len(message),1):
    print("message[",i,"]"," have ",message[i].count("a")," a")