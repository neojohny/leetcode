"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not root or not A or not B:
            return None
        
        if root == A:
            return A
        if root == B:
            return B
        
        al = self.inroot(root.left,A)
        ar = self.inroot(root.right,A)
        bl = self.inroot(root.left,B)
        br = self.inroot(root.right,B)
        if (al and br) or (ar and bl):
            return root
        if (al and bl):
            return self.lowestCommonAncestor3(root.left,A,B)
        
        if (ar and br):
            return self.lowestCommonAncestor3(root.right,A,B)
        
    
    def inroot(self,root,node):
        if not root or not node:
            return False
        
        if root == node:
            return True
        
        #if root.right:
        return self.inroot(root.right,node) or self.inroot(root.left,node)

