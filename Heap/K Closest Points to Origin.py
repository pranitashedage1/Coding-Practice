'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it 
is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = 0
        r = len(points) - 1

        while l <= r:
            ptr = self.partition(points, l, r)
            if ptr < k:
                l = ptr + 1
            elif ptr > k:
                r = ptr - 1
            else:
                return points[:k]
        
        return points[:l]

    def calculateDistance(self, points, index):
        return points[index][0]*points[index][0] + points[index][1]*points[index][1]

    def partition(self, points, l, r):
        pivot = points[r]
        p = l
        pivotDist = self.calculateDistance(points, r)
        for i in range(l, r):
            dist = self.calculateDistance(points, i)
            if dist <= pivotDist:
                if p != i:
                    points[p], points[i] = points[i], points[p]
                p += 1
        points[p], points[r] = pivot, points[p]
        return p


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         # using heap - 
#         heaplist = []
#         for pt in points:
#             sq = (pt[0]*pt[0]) + (pt[1] * pt[1])
#             heapq.heappush(heaplist, (sq, pt[0], pt[1]))
#         res = []
#         for _ in range(k):
#             temp = heapq.heappop(heaplist)
#             res.append([temp[1], temp[2]])
#         return res
            


