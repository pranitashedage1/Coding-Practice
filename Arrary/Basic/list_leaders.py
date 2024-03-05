# if there is higher number on the right side of the element then it is not a leader.
# l1 = [5, 3, 20, 15, 8, 3]
# o/p : [20, 15, 8, 3]
# last element will always be a leader.

l1 = [5, 3, 20, 15, 8, 25, 3]
for i in range(0, len(l1)-1):
    for j in range(i+1, len(l1)):
        if l1[j] > l1[i]:
            break
    else:
        print(l1[i])
print(l1[-1])

# Above solution is O(n2) but above solution can be done in O(n) time.
l1 = [5, 3, 20, 15, 8, 25, 3]
n = len(l1)-1
max = l1[n]
l2 = []
l2.append(l1[n])
for i in range(n-1, 0, -1):
    if l1[i] > max:
        max = l1[i]
        l2.append(max)
print(l2[::-1])
