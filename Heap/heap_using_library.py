from heapq import heapify, heappop, heappush, nlargest, nsmallest, heappushpop, heapreplace, merge
# from queue import PriorityQueue
import heapq

heap = []
heapify(heap)
heappush(heap, 20)
heappush(heap, 10)
heappush(heap, 12)
heappush(heap, 0)
heappush(heap, -3)

print("head value of the heap = ", str(heap[0]))

print("pring heap elements - ")
for i in heap:
    print(i, end=' ')

heappop(heap)
print("Printing the heap elements after heap pop - ")
for i in heap:
    print(i, end=' ')

# Gives first k smallest elements
# heapq.nsmallest(n, iterable, key=None)
#  Equivalent to sorted(iterable, key=key)[:n]
smallest_two = nsmallest(2, heap)
print("smallest two", smallest_two)


# Gives first k largest elements - 
# heapq.nlargest(n, iterable, key=None)
# Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
largest_three = nlargest(3, heap)
print("Largest 3 elements = ", largest_three)
print("===*******===========****************===================")
# N larges on dictionary :
print("# N largest on dictionary :")
dict1 = {1: 3, 2: 1, 3: 4}
print(heapq.nlargest(2, dict1.keys(), key=dict1.get))
print("===*******===========****************===================")

# Heappushpop - Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().
print("Before heappushpop", heap)
heappushpop(heap, -4)
print("Afterheappushpop", heap)
print("*****")
print("Before heappushpop", heap)
heappushpop(heap, 8)
print("Afterheappushpop", heap)
print("=======================")

# Heaprplace - Pop and return the smallest item from the heap, and also push the new item.
#  The heap size doesn’t change. If the heap is empty, IndexError is raised.
print("Before Heaprplace", heap)
heapreplace(heap, -4)
print("After Heaprplace", heap)
print("*****")
print("Before Heaprplace", heap)
heapreplace(heap, 8)
print("After Heaprplace", heap)
print("=======================")

# Check afterwards
# heapmerge - Merge multiple sorted inputs into a single sorted output. Returns an iterator over the sorted values.
# heapq.merge(*iterables, key=None, reverse=False)
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]
# Print in ascending order
merged_result = list(merge(list1, list2, list3))
print("Ascending order - ", merged_result)

# Print in Descending order
descending_merge = list(merge(list1, list2, list3, reverse=True))
print("Descending merge", descending_merge)
