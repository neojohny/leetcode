from collections import deque
class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        #groups = (set([0]),set(graph[0]))
        # groups = set()
        colors = {}#{0:0}
        
        q = deque(range(len(graph)))
        
        while q:
            node = q.popleft()
            #print('there')
            if node not in colors:
                colors[node] = 0
            
            for i in range(len(graph[node])):
                if graph[node][i] in colors:
                    if colors[graph[node][i]] == colors[node]:
                        #print('here')
                        return False
                        
                else:
                    
                    colors[graph[node][i]] = 1 - colors[node]
                    q.append(graph[node][i])
                    #groups.add(graph[node][i])
            #print(colors)
        return True
        