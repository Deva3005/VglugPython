# integer1 = int(input("Enter Number [No Alphabets or Symbols]\n"))

# def ReverseInt(number:int)->int:
#     if(number<0):
#         reversedInt = int(str(number)[1:][::-1])*-1
#         if(reversedInt < -(2**31) or reversedInt > (2**32)):
#             return 0
#         else:
#             return reversedInt
#     reversedInt1 = int(str(number)[::-1])
#     if(reversedInt1 < -(2**31) or reversedInt1 > (2**32)):
#             return 0
#     return reversedInt1

# print(
# ReverseInt(integer1))

number = int(input("Enter the Number [No Alphabets No Symbols]"))

def revNumber(number:int)->int:
    answer=0
    flag=False
    if number<0:
        number=abs(number)
        flag=True
    while number>0:
        answer=answer*10+number%10
        number//=10
    if(answer < -(2**31) or answer > (2**32)):
            return 0
    if flag:
        return answer*-1
    else:
        return answer

print(revNumber(number))