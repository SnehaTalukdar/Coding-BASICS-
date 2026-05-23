#Fibonacci Series
n = int(input("Enter the number of terms, required: "))
a = 0 #first number
b = 1 #second number

for i in range(n): #i goes to n times
    c = a+b #for next new term
    print(a , end = " ") #print like this with space
    #For next time
    a = b
    b = c

