# array is given, l1 = [2, 8, 3, 9, 6, 5, 4]
# if getsum(0, 2) is passed then it should send the sum of elements form index 0 to 2
# if getsum(3, 4) is passed then it should send the sum of elements form index 3 to 4

# this one is a simple apprach where for every query below loop will get execute
l1 = [2, 8, 3, 9, 6, 5, 4]
def add_int(start, end, l1):
    sum = 0
    for i in range(start, end+1):
        sum += l1[i]
    print(sum)

# This one uses a prefix sum approach. First calculate the prefix sum array of a given array.
s1 = ((3, 4), (0,2) , (2,3))
l1 = [2, 8, 3, 9, 6, 5, 4]

# get a prefixed array: which will be # l2 = [2, 10, 13, 22, 28, 33, 37]
l2 = [0]*len(l1)
sum = 0
for i in range(len(l2)):
    sum = sum + l1[i]
    l2[i] = sum
print(l2)

for i in range(len(s1)):
    if(s1[i][0] != 0):
        sum = l2[s1[i][1]] - l2[s1[i][0]-1]
    else:
        # for (0, 2) simply return the sum form the 2nd index position which is 13
        sum = l2[s1[i][1]]
    print(sum)
