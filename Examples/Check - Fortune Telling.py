'''
Given a collection of n cards. The i-th card (1 ≤ i ≤ n) has a number Ai on its front and a number Bi on its back. 
At the start, all the cards are facing upwards. He wants to minimize the range of numbers 
(i.e. the difference between the maximum and minimum values) on the face-up side. He is allowed to flip a maximum of m cards. 
Flipping a card will transition Bi to the face up side and Ai to the back. Help him find the minimum possible range
after using at most m flips.
Input
The first line of the input consists of 2 integers n and m . 
The next line contains n integers, i-th of which denotes Ai . 
The next line contains n integers, i-th of which denotes Bi .
Output
Output a single integer, the minimum possible range.

Example 1 :
Input: n = 5, m = 2, A = [1, 2, 17, 16, 9], B = [3, 4, 5, 6, 11]
Output: 8 
Explanation: By flipping card 3 and 4, we get the face up numbers {1, 2, 5, 6, 9}. This makes range=9-1=8.

Constraints:
1 <= m <= n
1 <= Ai, Bi <= 107
'''
def minimize_range(A, B, n, m):
    if A != B:
        values_to_change = {}
        for i in range(n):
            value_to_change = A[i] - B[i]
            values_to_change[i] = value_to_change

        for _ in range(m):
            max_value = float('-inf')
            index_to_change = 0

            for j in values_to_change:
                value = values_to_change[j]

                if value == 0:
                    continue

                if value == max_value:
                    if value > 0:
                        if A[j] > A[index_to_change]:
                            index_to_change = j
                            max_value = value
                    else:
                        if B[j] < B[index_to_change]:
                            index_to_change = j
                            max_value = value
                else:
                    if value > max_value:
                        max_value = value
                        index_to_change = j

            values_to_change[index_to_change] = 0
            A[index_to_change] = B[index_to_change]

    A.sort()

    return A[n - 1] - A[0]


# def minimize_range(n, m, A, B):
#     # Calculate the initial range with all A
#     initial_min = min(A)
#     initial_max = max(A)
#     initial_range = initial_max - initial_min

#     # Create a list of tuples (Ai, Bi)
#     cards = list(zip(A, B))
    
#     # Calculate the impact of flipping each card
#     impacts = []
#     for ai, bi in cards:
#         # The impact is how much we can potentially improve the range
#         # impact = abs(ai - bi)
#         impact = (ai - bi)
#         impacts.append((impact, ai, bi))
    
#     # Sort the impacts by the magnitude of impact in descending order
#     impacts.sort(reverse=True, key=lambda x: x[0])
    
#     # Choose the top m flips based on the impact
#     for i in range(m):
#         if impacts[i][1] == initial_min:
#             initial_min = impacts[i][2]
#         elif impacts[i][1] == initial_max:
#             initial_max = impacts[i][2]
        
#         # Update initial values to reflect the flip
#         cards[cards.index((impacts[i][1], impacts[i][2]))] = (impacts[i][2], impacts[i][1])
    
#     # After flipping m cards, calculate the new min and max
#     new_face_up_values = [ai for ai, bi in cards]
#     new_min = min(new_face_up_values)
#     new_max = max(new_face_up_values)
#     new_range = new_max - new_min
    
#     # Return the minimum possible range
#     return new_range

n = 5
m = 2
A = [1, 2, 17, 14, 9]
B = [3, 4, 5, 6, 11]
print(minimize_range(A, B, n, m))  # Output: 8

A = [10, 35, 27, 42, 19]
B = [13, 4, 5, 100, 8]
print(minimize_range(A, B, n, m))

A = [12, 34, 56, 104, 9]
B = [3, 4, 5, 100, 11]
print(minimize_range(A, B, n, m))
