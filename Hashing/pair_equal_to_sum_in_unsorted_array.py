# Given an unsorted array, and a number x, find if there is a pair with sum.
# i/p > arr = [3, 5, 2, 8, 11, 7], x = 16
#  o/p = True
#  create a set and check if x-arr[i] is present in the set, if yes then return true

arr = [3, 5, 2, 8, 11, 7]
x = 8
def check(arr, x):
    s1 = set()
    for i in arr:
        if x-i not in s1:
            s1.add(i)
        else:
            return True
    return False

a = check(arr, x)
print(a)
