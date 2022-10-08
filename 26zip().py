# Ass5 จับคู่สินค้ากับราคา
# zip()

fruit = ["mango","starwberri","grape"]
price = [50,30,15]

for x,y in zip(fruit,price): # fruit เก็บในตัวเเปร x / price เก็บในตัวเเปร y
    print("fruit: ",x," price: ",y)