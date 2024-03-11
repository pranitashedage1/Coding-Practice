'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()

        # This will keep index of last element from the array
        last_occurance = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            # we can only try to add c if it's not already in our solution
            # this is to maintain only one char in the res string

            if c not in seen:
                # if last letter form solution string is 
                #   i) exists
                #   ii) if greather than the c, so removing it will make the string smaller.
                #   iii) it's not the last occurrence
                # We remove it from the solution to keep the solution optimal.
                while stack and c < stack[-1] and i < last_occurance[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            
        return ''.join(stack)        

s = Solution()
print(s.removeDuplicateLetters('cbacdcbc'))
