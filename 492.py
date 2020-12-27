class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    dummyhead = Node()    
    curhead = dummyhead
    def enqueue(self, item):
        # write your code here
       self.curhead.nextval = Node(item)
       self.curhead = self.curhead.nextval
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        val = self.dummyhead.nextval.dataval
        self.dummyhead = self.dummyhead.nextval
        return val