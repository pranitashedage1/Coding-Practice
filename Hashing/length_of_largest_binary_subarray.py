# Given a binary array, find the length of the largest subarray having equal number of o and 1s.
# i/p = [0, 1, 1, 0, 1, 1, 0]
#  o/p = 4
#  i/p = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0]
#  o/p = 8

# Steps - 
#  i) convert all 0s to -1.
#  ii) Compute the prefix sum array
#  iii) Use a hashmap to store the first occurrence of each prefix sum.
#  iv) Iterate through prefix sum array.

arr = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0]
def check(arr):
    
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    print(arr)

    # compute new prefix sum array
    pre_arr = [0]
    presum = 0
    for i in arr:
        presum += i
        pre_arr.append(presum)
    print(pre_arr)

    # Use a hashmap to store the first occurrence of each prefix sum.
    dict1 = {}
    max_length = 0

    # Iterate through the prefix sum array
    for i in range(len(pre_arr)):
        current_sum = pre_arr[i]

        if current_sum in dict1:
            max_length = max(max_length, i-dict1[current_sum])
        else:
            dict1[current_sum] = i

    return max_length
    # Iterate thorough prefix sum array.

a = check(arr)
print(a)
