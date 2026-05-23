#largest and smallest elements
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Sorted array:", arr)

largest = arr[0] #initially 0th position element is considered as the largest
smallest = arr[0] #initially 0th position element is considered as the smallest

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest element is:", largest)
print("Smallest element is:", smallest)