#Frequency Count
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Array: ", arr) #Sorted array

visited = [] #empty list for visited elements

for i in arr: #sees the elements
    if i not in visited: #if i not visited already
        count = 0 #start initially as 0 
        for j in arr: #j goes throughout the whole array
            if i == j: #if our picked up element equals to j
                count += 1 #count = count + 1...increments count
        #after for j loop, coz we count the elements here
        print(i, "=", count) #element = it's count
        visited.append(i) #done this so that i value is not repeated. The already worked i element gets stored in the visitor list

