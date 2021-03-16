from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        #visited = [[0]*len(grid[0]) for i in range(len(grid[1]))]
        visited = set()
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (i,j) not in visited and grid[i][j]:
                    self.has_neighbour(grid,i,j,visited)
                    counter += 1
        return counter

    def has_neighbour(self,grid,x,y,visited):
        
        directions = [(0,1),(-1,0),(0,-1),(1,0)]

        q = deque([(x,y)])
        visited.add((x,y))
        while q:
            head = q.popleft()

            for a,b in directions:
                newx = head[0] + a
                newy = head[1] + b
                if not self.isvalid(newx,newy,grid,visited):
                    continue
                q.append((newx,newy))
                visited.add((newx,newy))
    
    def isvalid(self,x,y,grid,visited):
        if x > len(grid) -1 or y > len(grid[0]) -1 or x <0 or y<0:
            return False
        if (x,y) in visited:
            return False
        return grid[x][y]
