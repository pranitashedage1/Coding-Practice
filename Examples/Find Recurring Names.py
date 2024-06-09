'''
Amazon rewards its new users with a discount coupon that can be applied to their first purchase. Some users create more than one account in order to receive the offer multiple times. It was found that their new usernames are only a permutation of their real names.
For examples, if the real usernames of the users are realNames = ["abc", "def"] and the list of all usernames is allNames = ["bca", "abc", "cba", "def"] , then the user "abc" must have made multiple accounts as there are three permutations of "abc" in the list of all usernames.
Given an array of realNames an array allNames of usernames for each account, identify the names of users who created accounts more than once. The goal is to return the array of real names of these users in lexicographical order. If there are no such names, return an array containing only the string "None".
Please note that:
It is guaranteed that no two real names are permutations of each other.
For the variable realNames , each value is unique, and indicates an individual person.
Each name in allNames is a permutation of some name in realNames .
There may be some names in realNames without a permutation in allNames .
It is possible that some users may create an account using fake names only.

Function Description
Complete the function findRecurringNames in the editor.
findRecurringNames has the following parameters:
string realNames[n] : the real user names
string allNames[m] : all registered user names

Returns
string[] : the distinct real names of users with multiple registrations in lexicographical order

Example 1 :
Input: realNames = ["rohn", "henry", "daisy"], allNames = ["ryhen", "aisyd", "henry"]
Output: ["henry"] 
Explanation: "henry" occurs twice, as "ryhen" and "henry". A permutation of "daisy" occurs once and there are no permutations of "rohn".

Example 2 :
Input: realNames = ["tom", "jerry"], allNames = ["reyjr", "mot", "tom", "jerry", "mto"]
Output: ["jerry", "tom"] 
Explanation: "tom" occurs thrice as "mot", "tom", and "mto". "jerry" occurs twice as "reyjr" and "jerry".

Constraints:
1 ≤ n, m ≤ 10^5
1 ≤ |realNames[i]|, |allNames[i]| ≤ 10
Each name in realNames and allNames consists of lowercase English letters only.
'''
from collections import defaultdict
def findRecurringNames(realNames, allNames):
    result = []
    freq = defaultdict(int)
    for i in allNames:
        freq[''.join(sorted(i))] += 1
    
    for j in realNames:
        if freq[''.join(sorted(j))] > 1:
            result.append(j)
    
    result.sort()
    return result

realNames = ["rohn","henry","daisy"]
allNames = ["ryhen","aisyd","henry"]
print(findRecurringNames(realNames, allNames))


# from collections import defaultdict

# def findRecurringNames(realNames, allNames):
#     freq = defaultdict(int)
#     result = []
#     for i in allNames:
#         freq[''.join(sorted(i))] += 1
    
#     for j in realNames:
#         if freq[''.join(sorted(j))] > 1:
#             result.append(j)

#     result.sort()
#     return result

# realNames = ["rohn","henry","daisy"]
# allNames = ["ryhen","aisyd","henry"]
# print(findRecurringNames(realNames, allNames))
