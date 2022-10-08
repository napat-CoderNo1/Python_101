data = {"191":"police", "1668":"Hospital", "1447":"StopFireCar"}
data2 = {"191":"police", "1668":"Hospital", "1447":"StopFireCar"}

def searchNumber(message):
    check = False
    for key, value in data.items():
        if value == message:
            print("contract : ", key)
            check = True
    if check == False:
        print("NO contract")

searchNumber("police")
searchNumber("Hospital")
searchNumber("StopFireCar")
searchNumber("Batman")