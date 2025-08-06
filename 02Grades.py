marksAndGrades={
    range(91,101):"S",
    range(81,91):"A",
    range(71,81):"B",
    range(61,71):"C",
    range(51,61):"D",
    range(41,51):"E",
    range(0,41):"Fail",
}

mark = int(input("Enter Mark [allowed range 0-100]\n"))

if(mark<0):
    print("Given Value is Not worth it")
    exit(0)
for i in marksAndGrades.keys():
    if mark in list(i):
        print(marksAndGrades[i])
