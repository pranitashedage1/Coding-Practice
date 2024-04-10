'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # return num
        nums = list(str(num))
        buckets = [0] * 10
        # find the last index of each element
        for i in range(len(nums)):
            buckets[int(nums[i])] = i
        
        # for each digit, we will check if there exists any numger greater than it.
        for i in range(len(nums)):
            # for every number we will check if there is any number greater and its index is
            # greater than the current number index
            # if yes then swap the elements.
            for k in range(9, int(nums[i]), -1):
                max_index = buckets[k]
                if max_index > i:
                    nums[max_index], nums[i] = nums[i], nums[max_index]
                    return int("".join(nums)) 
        return num
