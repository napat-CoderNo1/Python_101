# สร้าง function รับค่า หาผลรวมตัวเลข

def sum(number):
    sum = 0
    for i in number:
        sum = sum+i
    print(sum)

x = [1,2,3,4,5,6,7,8]
sum(x)