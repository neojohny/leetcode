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
                        
        # numOfEdge = len(edges)
        # # 判断是否为 (n - 1) 条边
        # if numOfEdge != n - 1:
        #     return False
        # # adjacent[i]里存i的相邻点
        # adjacent = [[0] * n for _ in range(n)] 
        # for i in range(numOfEdge):
        #     u = edges[i][0]
        #     v = edges[i][1]
        #     adjacent[u][v] = adjacent[v][u] = 1
        # # visit[i]记录i是否被访问
        # visit = [0] * n
        # # 0作为根结点，开始向下遍历
        # visit[0] = 1
        # root, numOfVisited = 0, 1
        # q = collections.deque()
        # q.append(root)
        # while len(q) != 0:
        #     root = q.popleft()
        #     for i in range(n):
        #         if adjacent[root][i] != 1:
        #             continue
        #         # 如果相邻且没有被访问过，说明是儿子，加入队列
        #         if visit[i] == 0:
        #             visit[i] = 1
        #             numOfVisited += 1
        #             q.append(i)
        # if numOfVisited == n:
        #     return True
        # return False