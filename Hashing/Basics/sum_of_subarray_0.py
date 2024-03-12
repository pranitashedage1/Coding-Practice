# Given an array, find if there is a subarray with 0 sum.
# Crate a prefix sum and add in the set.
# If the prefix sum is already preset in the array then return true
# While creating a set, add 0 in the set to handle one scenario - {5, -5, 17} 
# {5, -5, 56}  In this 5 and -5 sum will be 0 but it won't return true as set does not have 0.

arr = [5, 6, -4, -2, 8, 10]
def check(arr):
    prefix_sum = 0
    s1 = {0}
    for i in arr: 
        prefix_sum += i
        if prefix_sum in s1:
            return True
        s1.add(prefix_sum)
    return False
a = check(arr)
print(a)
