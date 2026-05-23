#Prime Number checking
num = int(input("Enter any number:"))
flag = True #initially we take the number as a prime number
#first checking whether the num is less or equal or greater than i
if(num <= 1):
    flag = False #prime number must be greater than 1...so false when num is less or equal to 1
else: #for prime numbers(the nums which are greater than and not equal to 1)
    for i in range(2, num-1): #starts from 2 goes till the end
        if(num % i == 0):
            flag = False #i is not 1 or the number itself so no logic means flag will become as false
            break
    if flag:
        print("Prime Number")
    else:
        print("Not a Prime Number")

