from collections import OrderedDict

d1 = OrderedDict()
d1['test'] = 1
d1[34] = 'abcd'
d1['test1'] = 58
for i in d1:
    print(i, end = ' ')
d1.move_to_end('test')
print()
for i in d1:
    print(i, end = ' ')
