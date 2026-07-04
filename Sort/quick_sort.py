def quick_sort(arr, left, right):
    if left < right:
        # 1. Partition the array and get the pivot's final resting index
        pivot_pos = partition(arr, left, right)
        
        # 2. Recursively sort the left and right sub-arrays
        quick_sort(arr, left, pivot_pos - 1)

def partition(arr, left, right):
    pivot = arr[right]  # Choosing the last element as pivot
    i = left
    j = right - 1
    
    while i <= j:
        # Move 'i' right while elements are strictly less than pivot
        while i <= j and arr[i] < pivot:
            i += 1
            
        # Move 'j' left while elements are strictly greater than pivot
        while j >= left and arr[j] > pivot:
            j -= 1
            
        if i < j:
            # Swap misplaced elements
            arr[i], arr[j] = arr[j], arr[i]
            # Safely advance both pointers past the swapped elements
            i += 1
            j -= 1
        else:
            # If pointers meet or cross, break out to do the final pivot swap
            break

    # Final Pivot Swap: Place the pivot into its correct sorted position
    arr[i], arr[right] = arr[right], arr[i]
    
    return i  # Return the pivot's final index

# --- Verification ---
if __name__ == "__main__":
    arr = [22, 11, 88, 66, 55, 11, 77, 33, 44]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)