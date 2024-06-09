'''
Your company is developing a string matching library. You are to develop a service that finds the longest substring that matches a given regex.
More formally, you are given two strings, a text string text , and a regex expression regex . The string regex contains exactly one wildcard character(*). A wildcard character (*) matches any sequence of zero or more lowercase English characters. A regex matches some string if it is possible to replace the wildcard character with some sequence of characters such that the regex expression becomes equal to the string. No other character can be changed. For example, regex "abc*bcd" matches " abcbcd ", " abc efg bcd " and " abc c bcd ", whereas it does not match the strings " abc bd", "abz bcd ", " abc d".
Return the length of the longest substring of text that matches the expression regex . Return -1 if there is no such substring.
Note: A substring is a contiguous sequence of characters within a string.

Function Description
Complete the function getLongestMatch in the editor below.
getLongestMatch has the following parameters:
1. STRING text : a string
2. STRING regex : a string

Returns
int : the length of the longest substring that matches the regex, or -1 if there is no such substring.

Example 1 :
Input: text = "hackerrank", regex = "ack*r"
Output: 6 
Explanation: The following substrings match regex:
"acker", we can replace * with "e" and regex becomes equal to "acker". length = 5
"ackerr", we can replace * with "er" and regex becomes equal to "ackerr". length = 6
Return the length of the longest matching substring, 6.

Example 2 :
Input: text = "programming", regex = "r*in"
Output: 9 
Explanation: "rammin", len = 6. We can replace * with "amm" "rogrammin" len = 9. We can replace * with "ogramm"

Example 3 :
Input: text = "debug", regex = "ug*eb"
Output: -1 
Explanation: No substring of text begins with 'u' and ends with 'eb'

Constraints:
1 <= |text|, |regex| <= 106
text contains lowercase English letters only
regex contains lowercase English letters and exactly one wildcard(*) character
'''
# def getLongestMatch(text, regex):
#     # Split the regex into prefix and suffix parts
#     prefix, suffix = regex.split('*')
    
#     prefix_len = len(prefix)
#     suffix_len = len(suffix)
    
#     n = len(text)
    
#     # Find all starting positions of the prefix in text
#     prefix_positions = []
#     for i in range(n - prefix_len + 1):
#         if text[i:i+prefix_len] == prefix:
#             prefix_positions.append(i)
    
#     # If no prefix is found, return -1
#     if not prefix_positions:
#         return -1
    
#     max_length = -1
    
#     # For each prefix position, find the farthest suffix position
#     for start in prefix_positions:
#         for end in range(start + prefix_len, n - suffix_len + 1):
#             if text[end:end+suffix_len] == suffix:
#                 max_length = max(max_length, end + suffix_len - start)
#                 break  # Move to the next prefix position
    
#     return max_length

# # Example usage
# print(getLongestMatch("hackerrank", "ack*r"))  # Output: 6
# print(getLongestMatch("programming", "r*in"))  # Output: 9
# print(getLongestMatch("debug", "ug*eb"))       # Output: -1

def getLongestMatch(text, regex):
    # Split the regex into prefix and suffix parts
    prefix, suffix = regex.split('*')
    
    prefix_len = len(prefix)
    suffix_len = len(suffix)
    
    n = len(text)
    
    # Find all starting positions of the prefix in text
    prefix_positions = []
    for i in range(n - prefix_len + 1):
        if text[i:i+prefix_len] == prefix:
            prefix_positions.append(i)
    
    # If no prefix is found, return -1
    if not prefix_positions:
        return -1
    
    max_length = -1
    
    # For each prefix position, find the farthest suffix position
    for start in prefix_positions:
        # Try to find the suffix in the remaining part of the string
        for end in range(start + prefix_len, n - suffix_len + 1):
            if text[end:end+suffix_len] == suffix:
                max_length = max(max_length, end + suffix_len - start)
                break  # We want the first match after start, so we break
    
    return max_length

# Example usage
print(getLongestMatch("hackerrank", "ack*r"))  # Output: 6
print(getLongestMatch("programming", "r*in"))  # Output: 9
print(getLongestMatch("debug", "ug*eb"))       # Output: -1
