'''
Check after wards - https://leetcode.com/discuss/interview-question/5096695/Amazon-OA 
Amazon has multiple delivery centers for the distribution of its goods. 
In one such center, parcels are arranged in a sequence where the i i-th parcel has a weight of weight[i]. 
A shipment is constituted of a contiguous segment of parcels in this arrangement. 
That is, for 3 parcels arranged with weights 
[3,6,3][3,6,3], a shipment can be formed of parcels with weights 
[3,6][3,6], [6][6], [3,6][3,6], [6,3][6,3] and 
[3,6,3]
[3,6,3] but not with weights 
[3,3]
[3,3]. These shipments are to be loaded for delivery and must be balanced.
A shipment is said to be balanced if the weight of the last parcel of the shipment is not the maximum 
weight among all the weights in that shipment. For example, shipment with weights 
[3,9,4,7]
[3,9,4,7] is balanced since the last weight is 7, while the maximum shipment weight is 9. 
However, the shipment 
[4,7,2,7]
[4,7,2,7] is not balanced.
Given the weights of 
n parcels placed in a sequence, find the maximum number of shipments that can be formed such that 
each parcel belongs to exactly one shipment, each shipment consists of only a contiguous segment of parcels, 
and each shipment is balanced. If there are no balanced shipments, return 0.
Example 1 :

# Example usage
weights = [1, 2, 3, 2, 6, 3]
print(max_balanced_shipments(weights))  # Output: 2

'''
# weights = [1, 2, 3, 2, 6, 3]
# print(max_balanced_shipments(weights))  # Output: 2

# def max_balanced_shipments(weights):
#     n = len(weights)
#     count = 0
#     end = 1
#     while end < len(weights):
#         if weights[end] < weights[end-1]:
#             count += 1
#             end += 1
#         end += 1

#     return count


# print(max_balanced_shipments([1, 2, 3, 2, 6, 3]))
    





# def max_balanced_shipments(weights):
#     n = len(weights)
#     if n == 0:
#         return 0
#     i = 0
#     count = 0
#     while i < n:
#         max_weight = weights[i]
#         j = i
        
#         # Expand the shipment while it's balanced
#         while j < n and weights[j] <= max_weight:
#             max_weight = max(max_weight, weights[j])
#             j += 1
        
#         # Check if the last shipment found is balanced
#         if j < n and weights[j] < max_weight:
#             count += 1
#             i = j + 1
#         else:
#             i += 1
    
#     return count

# # Example usage
# weights = [1, 2, 3, 2, 6, 3]
# print(max_balanced_shipments(weights))  # Output: 2
