'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        result = []
        for char, count in stack:
            result.append(count * char)

        return ''.join(result)

print(Solution().removeDuplicates('deeedbbcccbdaa', k = 3))