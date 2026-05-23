#Factorial of a number
num = int(input("Enter Number: "))
fact = 1 #not 0 because value becomes 0
for i in range( 1, num+1): #from 1 to last but not including the last number
    fact = fact * i
print("Factorial of a number:", fact)