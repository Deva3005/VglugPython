def checkIsPrime(number:int)->bool:
    if number==0 or number==1:
        return False
    if number==2 or number==3:
        return True
    for i in range(2,int((number**0.5)+1)):
        if number%i==0:
            return False
    else:
        return True

for i in range(50):
    if checkIsPrime(i):
        if(i<9):
            print("0"+str(i)," this is a PRIME number")
        else:
            print(i," this is a PRIME number")