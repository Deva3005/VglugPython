number = 431
temp=431
answer=0
while temp>0:
    answer=answer*10+temp%10
    temp//=10
print(answer)