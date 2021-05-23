#merge sort function
def mergeSort(array):
    mid = len(array)//2

    left = array[:mid]
    right = array[mid:]

    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
        else:
            array[k] = right[j]
        k +=1

#array which needs to be sorted using merge sort
array = [45,78,65,12,56,75,95]