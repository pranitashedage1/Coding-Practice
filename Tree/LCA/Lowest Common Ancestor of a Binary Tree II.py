'''
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, 
p and q. If either node p or q does not exist in the tree, return null. 
All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "
The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has 
both p and q as descendants (where we allow a node to be a descendant of itself)". 
A descendant of a node x is a node y that is on the path from node x to some leaf node.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.

'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Helper function to find the lowest common ancestor
        def lca(node, p, q, present):
            # Base case: if node is None, return None
            if not node:
                return None

            # Recursively find LCA in left and right subtrees
            left = lca(node.left, p, q, present)
            right = lca(node.right, p, q, present)

            # If the current node is equal to p, mark p as present
            if p.val == node.val:
                present[0] = True
                return node
            # If the current node is equal to q, mark q as present
            elif q.val == node.val:
                present[1] = True
                return node

            # If one of the nodes is found in the left subtree, return it
            if not left:
                return right
            # If one of the nodes is found in the right subtree, return it
            elif not right:
                return left
            # If both nodes are found in different subtrees, return the current node as LCA
            else:
                return node

        # Initialize present list to track presence of p and q
        present = [False, False]
        # Find the LCA of p and q
        found_lca = lca(root, p, q, present)
        # If both p and q are present, return the LCA
        if present[0] and present[1]:
            return found_lca
        # Otherwise, return None
        return None
