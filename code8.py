#Reverse array
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Array: ", arr)

rev = [] #stores reverse elements
#range(start, stop, step)
for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])
print("Reversed Array:", rev)

              #OR

arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Array: ", arr)

print(arr[::-1])