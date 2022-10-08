# Function
def getBalance():
    print("Balance is : ", account)

def depositA(money):
    if not type(money) is int and not type(money) is float:
        raise Exception ("Enter number only")
    if money<=0:
        raise Exception ("enter positive number")
    print("A add money : ", money, " bath")
    account["mr.A"] += money

def withdrawFromA(money):
    if not type(money) is int and not type(money) is float:
        raise Exception ("Enter number only")
    if money<=0:
        raise Exception ("enter positive number")
    if money > account["mr.A"]:
        raise Exception ("Not enough money")
    print("A withdraw : ", money, " bath")
    account["mr.A"] -= money

def tranferToB(money):
    if not type(money) is int and not type(money) is float:
        raise Exception ("Enter number only")
    if money<=0:
        raise Exception ("enter positive number")
    if money > account["mr.A"]:
        raise Exception ("Not enough money")
    print("tranfer to B : ", money, " bath")
    account["mr.B"] += money
    account["mr.A"] -= money


# main program
account = {"mr.A":5000, "mr.B":0}

while True:
    try:
        getBalance()
        depositA(int(input("add : ")))
        getBalance()
        break
    except Exception as e:
        print(e)