'''
Given an integer n, return true if and only if it is an Armstrong number.
The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

Example 1:
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.

Example 2:
Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
'''
class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = []
        power = 0
        sum1 = 0
        N = n
        while N>0:
            nums.append(N%10)
            N //= 10
            power += 1
        
        for digit in nums:
            sum1 += digit ** power

        return n == sum1
