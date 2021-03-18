"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ''
        q = collections.deque([root])
        result = []
        while q:
            #level = []
            for _ in range(len(q)):
                head = q.popleft()
                result.append(str(head.val) if head is not None else '#')
                if head:
                    q.append(head.left)
                    q.append(head.right)
        return ' '.join(result)


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        slow, fast = 0, 1
        nodes = [TreeNode(d) if d != '#' else None for d in data.split(' ')] 
        while slow < len(nodes):
            if nodes[slow]:
                nodes[slow].left = nodes[fast]
                nodes[slow].right = nodes[fast+1]
                fast += 2
            slow += 1
            
        return nodes[0]

