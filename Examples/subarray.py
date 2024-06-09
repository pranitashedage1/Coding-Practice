'''
Amazon Web Services (AWS) has several processors for executing processes scheduled on its servers.

In order to maintain logical independence, a process is divided into segments. Each segment has two characteristics: the segment size (1 ≤ segment size ≤ 10⁹), and a pointer to the next segment so that the sequential order of execution is maintained within a process. Hence, this structure can be visualized as a linked list.

Given the segment structure of a process as a linked list, find the longest sub-list which has the segment sizes in non-increasing order. A sub-list of length 1 is always a valid sub-list. If there are multiple sub-lists of maximum length, return the sub-list which occurs earliest.

Note:
A sub-list is obtained by removing some nodes from the head and some nodes from the tail of the linked list.
Solve the problem in constant extra space.
Example

There are n = 5 segments with their segment sizes [2, 5, 4, 4, 5].

Segment Size 1	Segment Size 2	Segment Size 3	Segment Size 4	Segment Size 5
2	5	4	4	5
Output: [5, 4, 4]
'''

def check(nums):
    count = 1
    maxCount = 1
    start = 0
    end = 1
    maxStart = 0
    while end < len(nums):
        if nums[end] <= nums[end-1]:
            count += 1
        else:
            maxCount = max(count, maxCount)
            maxStart = start
            start = end
            count = 1
        end += 1
    maxCount = max(count, maxCount)
    return nums[maxStart:maxStart+maxCount]


nums = [2, 5, 4, 4, 5]
nums = [3, 2, 1, 4]
nums = [2, 2, 2, 2]
print(check(nums))
