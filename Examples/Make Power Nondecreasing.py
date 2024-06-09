'''
AWS provides scalable system. A set of n servers are used for horizontally scaling an application.
The goal is to have the computational power of the servers in non-decreasing order. To do so, you can increase the computational power of each server in any contiguous segment by x. Choose the values of x such that after the computational powers are in non-decreasing order , the sum of the x values is minimum.

Example 1 :
Input: power = [3, 4, 1, 6, 2]
Output: 7 
Explanation: Add 3 units to the subarray [2, 4] and 4 units to the subarray [4, 4,]. 
ans after adding first 3 into index [2, 4] > [3, 4, 4, 9, 5]
The final arrangement of the server is: [3, 4, 4, 9, 9]. The ans is 3 + 4 = 7. 
(As shown in the image) 

Constraints:
1 <= n <= 105
1 <= power[i] <= 109
'''
# def makePowerNonDecreasing(power):
#     n = len(power)
#     total_increament = 0
#     for i in range(1, n):
#         if power[i] < power[i-1]:
#             increament = power[i-1] - power[i]
#             power[i] += increament
#             total_increament += increament
#     return total_increament


def makePowerNonDecreasing(power):
    n = len(power)
    total_increament = 0
    i = 1
    while i < n:
        if power[i] < power[i-1]:
            increament = power[i-1] - power[i]
            for j in range(i, n):
                power[j] += increament
            total_increament += increament
        i += 1
    return total_increament

# Example usage:
power = [3, 4, 1, 6, 2]
print(makePowerNonDecreasing(power))  # Output: 7

# def makePowerNonDecreasing(power):
#     n = len(power)
#     total_increments = 0
    
#     for i in range(1, n):
#         if power[i] < power[i - 1]:
#             increment = power[i - 1] - power[i]
#             power[i] += increment
#             total_increments += increment
    
#     return total_increments

# # Example usage:
# power = [3, 4, 1, 6, 2]
# print(makePowerNonDecreasing(power))  # Output: 7
