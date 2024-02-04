# Find the most frequent element in the array (Repeated in array)
# This can be done using a dictionary.
#  i) O(n) - Insert in a dict if it is not already in the dict.
#     If an element is already in the dict then increment the value.
#  ii) O(n)Traverse the dict and find maximum value

arr = [5, 6, 5, -4, -2, -8, 10]
dict1 = {}
for i in arr:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
print(dict1)
flag = 1
max_value = dict1[arr[0]]
for key, value in dict1.items():
    if  value > max_value:
        max_value = value
        final = key
        flag = False

if flag:
    key = arr[0]
print(key)