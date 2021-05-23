def insertionSortAlgorithm(arr):
    for i in range(1, len(arr)): #1 means the 2 index of the array

        key = arr[i] #Assigning the key value of i
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

l =[]
for i in range(10):
    N = int(input())
    if N <= 20 and N >= 10:
        l.append(N)

print(l)
insertionSortAlgorithm(l)
print(l)