'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from collections import defaultdict
from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creating a dict to present the map
        adj_list = defaultdict(list)
        for prev in prerequisites:
            adj_list[prev[1]].append(prev[0])
        
        # Creating in_degree for each vertices
        in_degree = [0] * numCourses
        for pre in prerequisites:
            in_degree[pre[0]] += 1
        # initilizing count 
        count = 0
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            count += 1
            for v in adj_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        return count == numCourses

print(Solution().canFinish(numCourses=2, prerequisites=[[1,0],[0,1]]))
