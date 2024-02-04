# Peak element means element is not smaller that the neighbor elements

# arr = [5, 10, 20, 15, 17] - here 20 is the peak element
# arr = [10, 20, 15, 5, 23, 90, 67] - here 20 and 90 are the peak elements
# arr = [20, 5, 3] - here 20 is the peak element
# arr = [1, 5, 25] - here 25 is the peak element

arr = [0, 0, 2, 5, 23, 80, 67]

def peak_element(low, high, arr):
    mid = (low+high)//2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid] < arr [mid-1]:
        while mid > 0:
            mid = mid - 1 
            if mid == 0:
                return arr[mid]
            if arr[mid] > arr[mid-1]:
                return arr[mid]
    elif arr[mid] < arr[mid+1]:
         while mid < len(arr):
            mid = mid + 1 
            if mid == len(arr)-1:
                return arr[mid]
            if arr[mid] > arr[mid+1]:
                return arr[mid]

a = peak_element(0, len(arr)-1, arr)
print(a)
