# Given an unsorted array of non negative integers. Find if there is sub array with given sum.
# if there is a subarray with given sum, return True, else False
# sum = 33
# window sliding technique
l1 = [1, 1, 20, 3, 40, 5]
def check_subarray_sum(l1, final_sum):
    start = 0
    current_sum = l1[0]
    for end in range(1, len(l1)):
        while current_sum > final_sum and start < end: 
            current_sum = current_sum - l1[start]
            start = start + 1   
        if current_sum == final_sum:
            return True
        current_sum = current_sum + l1[end]
    if current_sum == final_sum:
        return True
a = check_subarray_sum(l1, 5)
print(a)
