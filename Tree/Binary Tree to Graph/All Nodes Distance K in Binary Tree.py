'''
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
'''
# Definition for a binary tree node.
from collections import defaultdict,deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.map = defaultdict(list)

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        res = []
        if root is None or k < 0:
            return res

        self.buildMap(root, None)

        q = deque([target])
        visited = set([target])

        # Normal BFS on the graph - 
        while q:
            n = len(q)
            if k == 0:
                while q:
                    res.append(q.popleft().val)
                return res
            for _ in range(n):
                node = q.popleft()
                for neighbor in self.map[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            k -= 1
        
        return res

    def buildMap(self, node, parent):
        if node is None:
            return

        if parent:
            self.map[parent].append(node)
            self.map[node].append(parent)
        
        self.buildMap(node.left, node)
        self.buildMap(node.right, node)
