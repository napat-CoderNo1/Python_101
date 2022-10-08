# จับคู่อีกเเบบนึง
'''
Hi  , Hello
ก้อง , เเก้ม

output Hi ก้อง , Hi เเก้ม , Hello ก้อง and Hello เเก้ม
'''
greeting = ["Hello","Hi","Good Morning"]
people = ["anna","jew","sense"]

# เเบบปกติ
for i in range(0,len(people),1):
    for j in range(0,len(greeting),1):
        print(greeting[j],people[i])
    print("-------------------------")

# เเบบลดรูป
result = [x+y for x in greeting for y in people]
print(result)
