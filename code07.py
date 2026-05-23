#second largest element
arr = list(map(int, input("Enter elements of array: ").split()))
arr.sort() #ascending order
print("Array:", arr)

largest = arr[0] #initially
second_largest = arr[0] #initially

for i in arr: # for finding the largest
    if i > largest:
        largest = i
for i in arr: # for finding the second largest
    if i > second_largest and i != largest:
        second_largest = i
print("Second Largest element is:", second_largest)

