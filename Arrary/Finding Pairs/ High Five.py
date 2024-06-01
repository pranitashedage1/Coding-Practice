'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

Example 1:
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

Example 2:
Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]
'''
from collections import defaultdict
from typing import List
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # initializing dictionary - to store scores of each student id
        dict1 = defaultdict(list)

        # Process each item from the input
        for item in items:
            student_id = item[0]
            score = item[1]

            # Insert the score into Max heap (inverted to use Python's min heap as max heap)
            heapq.heappush(dict1[student_id], -score)
        
        # Preaparing the result array array
        avg = []
        # We want the result array in a sorted format
        sorted_keys = sorted(dict1.keys())
        for student_id in sorted_keys:
            sum_of_5 = 0
            for _ in range(5):
                sum_of_5 += -heapq.heappop(dict1[student_id])
            avg.append([student_id, sum_of_5//5])

        return avg

