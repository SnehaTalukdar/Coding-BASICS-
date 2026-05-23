#Sum AND Average
arr = list(map(int, input("Enter elements of array: ").split()))
arr.sort()
print("Array: ", arr)

total = 0
for i in arr:
    total = total + i
    average = total / len(arr)

print("Sum is: ", total)
print("Average is: ", average)