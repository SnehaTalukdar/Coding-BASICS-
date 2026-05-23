#Palindrome Number
num = int(input("Enter any number:"))
Original = num #user given number is the original one
reverse = 0 #initially reversed part is 0
while num > 0:
    num % 10 #taking last digits
    reverse = reverse + (num%10) #last  reverse value + num%10 value

if(Original == reverse):
    print("Palindrome")
else:
    print("Not Palindrome")