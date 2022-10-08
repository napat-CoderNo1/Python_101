def hanoi(n, tower1, tower2, tower3):
    if (n==0):
        return
    hanoi(n-1, tower1, tower3, tower2)
    print("จานที่ ", n, " ย้ายจากเสา ", tower1, " ไป ", tower3)
    hanoi(n-1, tower2, tower1, tower3)

hanoi(3,"A","B","C")