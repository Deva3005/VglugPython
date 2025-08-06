x,y=map(int,input("Enter the number x and y seperated by ',' \n").split(","))

operatorX=input("Choose the Operation [Allowed inputs :: +, -, *, /, **, //, %]\n")

if operatorX in "+, -, *, /, **, //, %".split(", "):
    if(operatorX=="+"):
        print("Operation: Addition")
        print(x+y)
    elif(operatorX=="-"):
        print("Operation Subtraction")
        print(max(x,y)-min(x,y))
    elif(operatorX=="*"):
        print("Operation: Multipplication")
        print(x*y)
    elif(operatorX=="/"):
        print("Operation: Division")
        print(x/y)
    elif(operatorX=="**"):
        print("Operation: Exponential")
        print(x**y)
    elif(operatorX=="//"):
        print("Operation: Integer Floor Division")
        print(x//y)
    elif(operatorX=="*"):
        print("Operation: Modulo Division")
        print(x%y)
    else:
        print("[Critical Logic Error]Operator INVALID")
else:
    print("Kindly Enter only Allowed Inputs")