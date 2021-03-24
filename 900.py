"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None

        if root.val == target:
            return root.val
        if root.val < target:
            

            if root.right:
                right = self.get_min(root.right)
                if target - root.val < right - target:
                    return root.val
                else:
                    return self.closestValue(root.right,target)
            else:
                return root.val
        
        else:
            if root.left:
                left = self.get_max(root.left)
                if target - left > root.val - target:
                    return root.val
                else:
                    return self.closestValue(root.left,target)
            else:
                return root.val


    def get_max(self,root):
        if not root.right:
            return root.val
        
        if root.right:
            return self.get_max(root.right)

    def get_min(self,root):
        if not root.left:
            return root.val
        
        if root.left:

            return self.get_min(root.left)