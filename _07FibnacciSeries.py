# OLD School recursion Technique

def fibonacciSeries(length:int):
    if length == 0 or length ==1:
        return 1
    else:
        return fibonacciSeries(length-1)+fibonacciSeries(length-2)
answer=[]
lengthFS = int(input("Enter the length of the Series [Non Negative and Non Zero]...\n"))
for i in range(lengthFS):
    answer.append(fibonacciSeries(i))

print(*answer)

#++++++++++++++++++++++++++++++++++++++++++++++

# using List Slice Ops

box=[1,1]

for i in range(lengthFS-2):
    box.append(box[-1]+box[-2])

print(*box)