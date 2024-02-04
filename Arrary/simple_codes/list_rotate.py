l1 = [2, 45, 78, 111, 99, 0, 78]
d = 2
# print(l1[d:]+l1[:d])

# reverse the arrary - 

l1[:d] = reversed(l1[:d])
l1[d:] = reversed(l1[d:])
l1 = reversed(l1)

print(l1)
