'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
 

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []

'''
# Delete the node in BST
#  Time Complexity - O(h)
#  Auxiliary Space -  O(h) Since it is a recursive function
# Binary Tree Implementation:
# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # Base Case: If the tree is empty
        if not root:
            return None
        # Otherwise, recur down the tree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.val = self.getMin(root.right)
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.val)
    
        return root

    def getMin(self, root):
        minV = root.val
        while root.left is not None:
            minV = root.left.val
            root = root.left
        return minV

def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.val, end =' ')
    printInorder(node.right)


if __name__ =='__main__':
    #  create a Node
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(7)
    root.left.right = Node(9)
    root.right.left = Node(11)
    root.right.right = Node(11)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    root.right.right.right = Node(18)

    printInorder(root)
    a = Solution().deleteNode(root, 12)
    print(a)
    printInorder(root)
