'''
There were a large number of orders placed on Prime Day. The orders are packed and are at the warehouse ready to be delivered. The delivery agent needs to deliver them in as few trips as possible.
In a single trip, the delivery agent can choose packages following either of two rules:
Choose two packages with the same weight
Choose three packages with the same weight
Determine the minimum number of trips required to deliver the packages. If it is not possible to deliver all of them, return -1.

Example 1:
Input: packageweight = [1, 8, 5, 8, 5, 1, 1]
Output: 3
Explanation:
It takes 3 trips to deliver all the packages.

Example 2:
Input: packageweight = [3, 4, 4, 3, 1]
Output: -1
Explanation:
Packages with weights 3 and 4 can be removed in groups of two. The package of weight 1 cannot be delivered as it cannot be chosen according to the rules. Since it is not possible to deliver all packages, the answer is -1.

Example 3:
Input: packageweight = [2, 4, 6, 6, 4, 2, 4]
Output: 3
Explanation:
The agent needs a min of 3 trips as shown below. Return 3 as the answer.
Function Description
Complete the function findMinTrips in the editor.
findMinTrips has the following parameter:
int packageweight[n]: the weights of each package

Returns
int: the minimum number of trips required or -1 if it is not possible to deliver them all

Constraints
1 <= n <= 105
0 <= packageweight[i] <= 109
'''
def findMinTrips(packageweight):
    from collections import Counter
    
    # Count the frequency of each weight
    weight_count = Counter(packageweight)
    
    trips = 0
    
    for weight, count in weight_count.items():
        # If there are not enough packages to form a pair or triplet, return -1
        if count == 1:
            return -1
        
        # Calculate the number of trips needed for this weight
        # We prefer triplets first because they are more efficient
        trips += count // 3
        remaining = count % 3
        
        if remaining == 1:
            # If we have one remaining package, we cannot deliver it
            # directly. We need to pair it with two more packages, thus we need one more trip.
            return -1
        elif remaining == 2:
            # If we have two remaining packages, we need one more trip
            trips += 1

    return trips

# Example usage
packageweight1 = [1, 8, 5, 8, 5, 1, 1]
print(findMinTrips(packageweight1))  # Output: 3

packageweight2 = [3, 4, 4, 3, 1]
print(findMinTrips(packageweight2))  # Output: -1

packageweight3 = [2, 4, 6, 6, 4, 2, 4]
print(findMinTrips(packageweight3))  # Output: 3
