# l1 = [1, 5, 3, 8, 12]
# find the maximum profit that can be achieved from this - 
# buy at 1, sale at 5, total profilt will be 4
# again buy at 3 and sale it at 12, total profit will be 12 - 3 = 9


l1 = [4, 3, 1, 2, 12, 5, 6, 7, 8, 9, 11, 3, 2, 9]
profit = 0
for i in range(1, len(l1)):
    if l1[i] > l1[i-1]:
        profit = profit + (l1[i] - l1[i-1])
print(profit)
