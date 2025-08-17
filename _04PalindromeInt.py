from _03reverseInt import revNumber

number1 = int(input("Enter the Number to check Palindrome...\n"))
if number1== revNumber(number1):
    print("Yes, it is Palindrome")
else:
    print("No, Not a Palindrome")