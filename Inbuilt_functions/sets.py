set1 = set()
print(type(set1))
s1 = {3, 4, 5}
s1.add(3) # Adds element in the set - takes only one element and Returns None,
# Even if you add existing element, it won't fail
s1.add(9)
# s1.add(56)
print(s1)
