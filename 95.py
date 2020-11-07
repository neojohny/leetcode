"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.check(root)[0]
        
        
        
        
    def check(self,root):
        if not root:
            return True,None,None
        
        leftisbst,leftmin,leftmax = self.check(root.left)
        rightisbst,rightmin,rightmax = self.check(root.right)
        
        if not leftisbst or not rightisbst:
            return False,None,None
            
        if leftmax and leftmax >= root.val:
            return False,None,None
        
        if rightmin and rightmin <= root.val:
            return False,None,None
        
        rootmin = leftmax if leftmax else root.val
        rootmax = rightmin if rightmin else root.val
        return True,rootmin,rootmax