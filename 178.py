class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges)!=n-1:
            return False
        graph = [[0]*n for _ in range(n)]
        for x,y in edges:
            graph[x][y] = 1
            graph[y][x] = 1
        
        q = collections.deque()
        visited = [0] * n
        visited[0] = 1
        root = 0
        beento = 1
        q.append(0)
        while q:
            #for _ in range(len(q)):
                root = q.popleft()
                for i in range(n):
                    if graph[root][i] == 0:
                        continue
                    if visited[i] == 0:
                        q.append(i)
                        visited[i] = 1
                        beento += 1
        return beento == n