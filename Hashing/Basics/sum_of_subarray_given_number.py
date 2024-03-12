# Given an array and sum x, find if there is a subarray whose sum is equal to x.
# # Create a prefix sum and add in the set.
# If the (prefix_sum-x)is already present in the array then return true

arr = [5, 3, 8, -2, 8, 10]
x = 11
def check(arr, x):
    prefix_sum = 0
    s1 = {0}
    for i in arr: 
        prefix_sum += i
        if (prefix_sum-x) in s1:
            return True
        s1.add(prefix_sum)
    return False
a = check(arr, x)
print(a)
