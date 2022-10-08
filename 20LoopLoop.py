# Loop while ซ้อน Loop while

i = 1

while i<=3 :
    j=1 # กำหนดค่า j ให้เป็น 1 เสมอ ก่อนเข้าไปวนใน loop => while j<=5 
    
    while j<=5 :
        print("Round: ",i," rank: ",j)
        if j==5 :
            print("\n")
        j+=1
    
    i+=1