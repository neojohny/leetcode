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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        if not self.isBalanced(root.right):
            return False
        if not self.isBalanced(root.left):
            return False
                
        l = self.depth(root.left)
        r = self.depth(root.right)
        if abs(l-r) > 1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.right)


    def depth(self,root):
        level = 0
        if not root:
            return level
        
        #level += 1
        r = 0
        l = 0
        if root.right:
            r = self.depth(root.right)
        if root.left:
            l = self.depth(root.left)
        
        return max(r,l) + 1