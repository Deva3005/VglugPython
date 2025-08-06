year=int(input("Enter the Year\n"))

if((year%4==0) and (year%100!=0)) or year%400==0:
    print(f"Given {year} is Leap Year!!!")
else:
    print(f"Given {year} is not a Leap Year")
        