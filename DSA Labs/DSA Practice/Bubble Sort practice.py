def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

array = [45,78,65,12,56,75,95]
bubbleSort(array)
print(array)