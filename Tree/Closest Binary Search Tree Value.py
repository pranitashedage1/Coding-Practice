'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

Example 1:

     4
    / \
   2   5 
  / \
 1   3 
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Time complexity - O(N)
# Space complexity - O(N)
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return min(inorder(root), key = lambda x: abs(target - x))

# Time complexity - O(k) in average case, where tree is balanced
# O(H + K) in worst case, where k is an index of the closest element.
# Space complexity - O(H) - To keep the stack in the case of non balanced tree.
class Solution1:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if (prev <= target and target < root.val):
                return min(prev, root.val, key = lambda x: abs(target - x))
            prev = root.val
            root = root.right
        return prev

# Time complexity - O(H) since one is going to root, down to the leaf
# Space complexity - O(1)
class Solution2(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
            
        return closest

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    # print(Solution().closestValue(root, 3.714))
    # print(Solution1().closestValue(root, 3.714))
    print(Solution2().closestValue(root, 3.714))
