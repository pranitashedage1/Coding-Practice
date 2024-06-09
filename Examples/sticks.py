'''
Maximum area of all possible rectangles that can be formed. The twist here is that you can also reduce any element by atmost 1. find the maximum area of all the rectangles that can be fomed.

Note: One element can only be used once to form a single rectangle.

Input1: n = 8 arr[] = [2,3,3,4,6,6,8,8]
Output: 54
Explanation: There are two rectangles that can be formed one with edges [6,6,8,8] and another with by reducing 4 by 1 to 3 and reducing 3 by 1 to 2 so the edges will [2,2,3,3]
Therefore 6 * 8 + 2 * 3 = 54

Input2: [2,1,6,5,4,4]
Output: 20
Explanation: Here just 1 rectangle is possible with maximum by reducing 6 with 5 and hence 5*4 = 20

Please let me know how we can do this.
'''
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
