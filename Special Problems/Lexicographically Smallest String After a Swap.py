'''
Given a string s containing only digits, return the 
lexicographically smallest string that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, 
have the same parity, while 6 and 9 do not.

 

Example 1:
Input: s = "45320"
Output: "43520"

Explanation:
s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:
Input: s = "001"
Output: "001"

Explanation:
There is no need to perform a swap because s is already the lexicographically smallest.

Constraints:
2 <= s.length <= 100
s consists only of digits.
'''
class Solution:
    def getSmallestString(self, s: str) -> str:
        num = list(s)
        for i in range(0, len(num)-1):
            if int(num[i])%2 == 0 and int(num[i+1])%2 == 0 and int(num[i+1]) < int(num[i]):
                num[i+1], num[i] = num[i], num[i+1]
                break

            if int(num[i])%2 != 0 and int(num[i+1])%2 != 0 and int(num[i+1]) < int(num[i]):
                num[i+1], num[i] = num[i], num[i+1]
                break
        return ''.join(num)

