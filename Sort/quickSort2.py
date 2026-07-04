def quickSort(arr, left, right):
    while left < right:
        position_point = quickSort(arr, left, right)
        quickSort(arr, position_point + 1, right)
        quickSort(arr, left, position_point-1)
    

def partition(arr, left, right):
    i, j = left, right-1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        
        while j > left and arr[j] > pivot:
            j -= 1
        
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[i], arr[right] = arr[right], arr[i]
    return i

    

arr = [56, 34, 23, 78, 12, 67, 45]
left, right = 0, len(arr)-1


