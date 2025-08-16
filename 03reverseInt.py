integer1 = int(input("Enter Number [No Alphabets or Symbols]\n"))

def ReverseInt(number:int)->int:
    if(number<0):
        reversedInt = int(str(number)[1:][::-1])*-1
        if(reversedInt < -(2**31) or reversedInt > (2**32)):
            return 0
        else:
            return reversedInt
    reversedInt1 = int("-"+str(number)[::-1])
    if(reversedInt1 < -(2**31) or reversedInt1 > (2**32)):
            return 0
    return reversedInt

print(
ReverseInt(integer1))