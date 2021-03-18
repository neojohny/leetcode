"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        indegrees = self.get_nodes(graph)
        heads = [x for x in indegrees if indegrees[x] == 0]
        q = collections.deque(heads)
        result = []
        while q:
            head=q.popleft()
            result.append(head)
            for n in head.neighbors:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)
        
        return result



    def get_nodes(self,graph):
        #q = collections.deque([graph])
        result = {x:0 for x in graph}
        for head in graph:
            for n in head.neighbors:
                result[n] += 1
        return result