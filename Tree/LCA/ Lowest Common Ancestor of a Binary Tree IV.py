'''
Given the root of a binary tree and an array of TreeNode objects nodes, 
return the lowest common ancestor (LCA) of all the nodes in nodes. 
All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of
 n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant 
 (where we allow a node to be a descendant of itself) for every valid i". 
 A descendant of a node x is a node y that is on the path from node x to some leaf node.
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
Output: 1
Explanation: The lowest common ancestor of a single node is the node itself.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
Output: 5
Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
'''
class Solution:
    # def __init__(self):
    #     self.lca = None

    def lowestCommonAncestor(self, root, nodes):
        # Function to recursively find the lowest common ancestor
        def lca(node, node_val):
            # If node is None or if it's one of the target nodes, return the node
            if not node or node.val in node_val:
                return node

            # Recursively find LCA in left and right subtrees
            left = lca(node.left, node_val)
            right = lca(node.right, node_val)

            # If one of the nodes is found in the left subtree, return it
            if not left:
                return right
            # If one of the nodes is found in the right subtree, return it
            if not right:
                return left

            # If both nodes are found in different subtrees, return the current node as LCA
            return node

        # Create a set to store the values of target nodes
        node_val = set([node.val for node in nodes])
        # Call the helper function to find the LCA
        return lca(root, node_val)
