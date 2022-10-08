while True:
    try:
        number1 = int(input("Enter number1 : "))
        number2 = int(input("Enter number2 : "))
        result  = number1/number2
        
        # ถ้าไม่ error ถึงจะมาทำ 2 บรรทัดข้างล่างนี้ เเล้ว break ออกจาก loop
        print(result)
        break
    except Exception as e:
        print(e)
    finally:
        print("I don't care")