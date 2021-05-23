def selectionSort(array):
    n = len(array)
    for j in range(n-1):
        smallest = j
        for i in range(j+1, n):
            if array[i] < array[smallest]:
                smallest = i
        array[smallest], array[j] = array[j], array[smallest]

array = [45,78,65,12,56,75,95]
selectionSort(array)
print(array)