'''
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        currentStr = ''
        self.findpaths(root, paths, currentStr)
        return paths

    def findpaths(self, root, paths, currentStr):
        if not root:
            return
        
        if root.left is None and root.right is None:
            currentStr += str(root.val)
            paths.append(currentStr)


        if root.left:
            self.findpaths(root.left, paths, currentStr+str(root.val)+'->')

        if root.right:
            self.findpaths(root.right, paths, currentStr+str(root.val)+'->')
