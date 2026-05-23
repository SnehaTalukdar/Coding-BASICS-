#Armstrong Number
num = int(input("Enter any nuumber:"))
temp = num #temporary storing of the number
sum = 0 #initially sum is taken as 0
digits = len(str(num)) #digits gives number of digits which is = POWER VALUE

while temp > 0: #number should be more than 0
    digit = temp % 10 #takes last digit
    sum = sum + digit ** digits #sum = last sum value + digit^power
    temp = temp // 10 #to cut off last digit
if (sum == num):
    print("Armstrong Number")
else:
    print("Not an Armstrong number")