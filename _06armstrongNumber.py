number=input('Enter the Number [non-negative & non-zero number]\n')

def checkArmStrongNumber(number:str):

    if int(number)<=0:
        print("False Input I Repeat False Input...")
        exit(0)

    if int(number) == sum(list(map(lambda x:x**3,list(map(int,list(number)))))):
        print(number," The Given is Armstrong Number")
    else:
        print(number, " The Given is not an Armstrong Number")

checkArmStrongNumber(number=number)