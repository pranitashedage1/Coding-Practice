'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
'''
from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = defaultdict(int)

        # init topo map & indegree
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []

        # build topo map & indegree
        for curr, prev in prereq:
            indegree[curr] += 1
            graph[prev].append(curr)

        queue = deque()

        # add all the indegree=0 to queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # maintain count/flag to check cycle
        count = 0
        while queue:
            prev = queue.popleft()
            res.append(prev)
            count += 1
            for curr in graph[prev]:
                indegree[curr] -= 1
                # indegree will act as a visited list. We will visit the node again till the indegree is 0
                if indegree[curr] == 0:
                    queue.append(curr)

        # check for cycle if there is cycle count < numCourses
        if count == numCourses:
            # return resL
            return res
        else:
            return []
        
print(Solution().findOrder(2, [[1, 0]]))
