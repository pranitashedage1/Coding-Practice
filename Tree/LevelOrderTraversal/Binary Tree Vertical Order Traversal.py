'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
'''
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        col = deque()
        result = []
        minCol, maxCol = 0, 0
        colMap = defaultdict(list)
        q.append(root)
        col.append(0)
        while q:
            node = q.popleft()
            colN = col.popleft()
            colMap[colN].append(node.val)
            if node.left:
                q.append(node.left)
                col.append(colN - 1)
                minCol = min(minCol, colN - 1)
            if node.right:
                q.append(node.right)
                col.append(colN + 1)
                maxCol = max(maxCol, colN + 1)
        for i in range(minCol, maxCol+1):
            result.append(colMap[i])
        return result
