'''
Amazon would like to know how much inventory exists in their closed inventory compartments. 
Given a string s consisting of items as "* and closed compartments as an open and close " "
an array of starting indices startindices, and an array of ending indices endindices, 
determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk ('*'= ascii decimal 42)
A compartment Is represented as a pair or pipes that may or may not have items between them 
('I'= ascii decimal 124)
Example
S= '|**|*|*'
startindices = [1, 1]
endindices = [5, 6]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. 
For the first pair of indices, (1, 5), the substring is '|**|*'There are 2 items in a compartment
For the second pair of indices, (1, 6), the substring is '|**|*|*' and there are 2 + 1 = 3 items in compartments.
Both of the answers are returned in an array [2,3]

Function Description.
Complete the numberOfitems function in the editor below. The function must return an integer arrav that 
contains the results for each of the startIndices[i] and endindices(i] pairs.

numberOfltems has three parameters:

S: A string to evaluate
startindices: An integer arrav, the starting indices
endindices: An integer array, the ending indices.
Constraints

1 <= m, n <= 10^5
1 <= startindices[i] <= endindices[i] <= n
Each character of s is either '*' or '|'
Sample Input 1

S = '*|*|'
startIndices = [1]
endIndices = [3]
Sample Output 1 
0

Explanation
The substring from index = 1 to index = 3 is '*|*' There is no compartments In this string

Sample Input 2

S = '*|*|*|'
startIndices = [1]
endIndices = [6]
Sample Output 2
2

Explanation
The substring from index = 1 to index = 3 is '*|*|*|' There are two compartments in this string at 
(index = 2, index = 4) and (index = 4, index = 6). There are 2 items between these compartments.
'''
def numberOfItems(s, startIndices, endIndices):
    n = len(s)
    prefix_items = [0] * (n + 1)
    nearest_left_pipe = [-1] * n
    nearest_right_pipe = [-1] * n
    
    # Calculate prefix sum of items and nearest left pipe
    last_pipe = -1
    for i in range(n):
        if s[i] == '|':
            last_pipe = i
        nearest_left_pipe[i] = last_pipe
        prefix_items[i + 1] = prefix_items[i] + (1 if s[i] == '*' else 0)
    
    # Calculate nearest right pipe
    last_pipe = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_pipe = i
        nearest_right_pipe[i] = last_pipe
    
    result = []
    for start, end in zip(startIndices, endIndices):
        # Convert to 0-based index
        start -= 1
        end -= 1
        
        left_pipe = nearest_right_pipe[start]
        right_pipe = nearest_left_pipe[end]
        
        if left_pipe == -1 or right_pipe == -1 or left_pipe >= right_pipe:
            result.append(0)
        else:
            result.append(prefix_items[right_pipe + 1] - prefix_items[left_pipe + 1])
    return result

# Sample usage
S = '*|*|*|'
startIndices = [1]
endIndices = [6]
print(numberOfItems(S, startIndices, endIndices))  # Output: [2]

S = '*|*|'
startIndices = [1]
endIndices = [3]
print(numberOfItems(S, startIndices, endIndices))  # Output: [0]

S = '*|*|***|**|||*|*||||'
startIndices = [3]
endIndices = [14]
print(numberOfItems(S, startIndices, endIndices))  # Output: [0]
