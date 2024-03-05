l1 = [2, 4, 6, 1, 0, 34, 45]
# low = 0
# high = len(l1) - 1
# def swap(a, b, l1):
#     temp = l1[a]
#     l1[a] = l1[b]
#     l1[b] = temp
# while(low<high):
#     swap(low, high, l1)
#     low += 1
#     high -= 1
# print(l1)


# reverse the list with the recursion

def reverse_list(a, b, l1):
    if a >= b:
        return
    l1[a], l1[b] = l1[b], l1[a]
    reverse_list(a+1, b-1, l1)


reverse_list(0, len(l1)-1, l1)
print(l1)

