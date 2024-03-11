'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, 
you may assume that the original data does not contain any digits and that digits are only for 
those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        # Create two stack
        str_stack = []
        count_stack = []
        # Initialize a result list and count variable
        res = []
        count = 0
        # Below are condition - 
        #  i) when i is digit - add in the count
        #  ii) when i is '['
        #  iii) when i is ']'
        #  iv) when i is 'a'
        for c in s:
            if c.isdigit():
                count = count * 10 + int(c)
            elif c == '[':
                str_stack.append(''.join(res))
                count_stack.append(count)
                # Reset to the original values
                res = []
                count = 0
            elif c == ']':
                # Start poping
                last = str_stack.pop()
                repeat = count_stack.pop()
                res = [last +repeat * ''.join(res)]
            else:
                res.append(c)

        return ''.join(res)

# Example usage
solution = Solution()
print(solution.decodeString("3[a2[c]]"))  # Output: "accaccacc"
