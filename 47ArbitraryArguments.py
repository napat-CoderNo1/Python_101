# *args => มีชนิดข้อมูลเป็น Tuple
# กำหนด parameter ได้ไม่จำกัด

def add(*args): # จะเปลื่ยนเป็น * เเล้วตามด้วยตัวเเปรอะไรก็ได้ไม่จำเป็นต้องเป็น args เสมอไป
    print(args)

add()
add(10, 20)
add(True, "uzy", 10)

print("\n")

# แเล้วถ้าต้องการผลรวมตัวเลขล่ะ

def add2(*number):
    sum = 0
    for i in range(0, len(number), 1): # เขียน for i in number เเล้วเปลื่ยน number[i] => i ได้เลย
        sum = sum+number[i]
    print(sum)

add2(10, 20)
add2(10, 10, 10)
add2(10)