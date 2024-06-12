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

        # Initialize an empty list to store the result
        res = []
        # Create a graph to represent the relationships between courses
        graph = defaultdict(list)
        # Create a dictionary to store the indegree of each course
        indegree = defaultdict(int)

        # Initialize topo map & indegree
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []

        # Build topo map & indegree
        for curr, prev in prerequisites:
            indegree[curr] += 1
            graph[prev].append(curr)

        # Initialize a queue to store courses with zero indegree
        queue = deque()

        # Add all the courses with indegree=0 to the queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Initialize a count variable to track the number of courses processed
        count = 0
        while queue:
            # Remove a course from the queue
            pre = queue.popleft()
            # Add the course to the result list
            res.append(pre)
            # Increment the count of processed courses
            count += 1
            # Update the indegree of courses that are prerequisites for the current course
            for curr in graph[pre]:
                # Decrement the indegree
                indegree[curr] -= 1
                # If the indegree becomes zero, add the course to the queue
                if indegree[curr] == 0:
                    queue.append(curr)

        # Check for cycle: if there is a cycle, count will be less than numCourses
        if count == numCourses:
            return True
        else:
            return False

print(Solution().canFinish(2, [[1, 0]]))