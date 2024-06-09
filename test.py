def max_rectangle_area(arr):
    arr.sort()
    pairs = []
    i = len(arr) - 1

    while i > 0:
        if arr[i] == arr[i - 1] or arr[i] - 1 == arr[i - 1]:
            pairs.append(arr[i - 1])
            i -= 1
        i -= 1

    pairs.sort(reverse=True)

    max_area = 0
    for j in range(0, len(pairs) - 1, 2):
        max_area += pairs[j] * pairs[j + 1]

    return max_area

# Test cases
print(max_rectangle_area([2, 3, 3, 4, 6, 6, 8, 8]))  # Output: 54
# print(max_rectangle_area([2, 1, 6, 5, 4, 4]))        # Output: 20
