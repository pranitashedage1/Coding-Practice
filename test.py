from collections import Counter
s = 'abbacdeefaad'
print(Counter(s))
pq = [(-count, char) for char, count in Counter(s).items()]
print(pq)