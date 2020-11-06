from collections import deque
directions = [(1,0),(-1,0),(0,1),(0,-1)]
DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        

        
        if not grid:
            return 0
        
        q = deque()
        ans = 0
        check = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append((i,j))
                    path = ''
                    grid[i][j] = 0
                    while q:
                        x,y = q.popleft()
                        for dx,dy in directions:
                            newx=x+dx
                            newy=y+dy
                            if self.isvalid(grid,newx,newy):
                                grid[newx][newy]=0
                                path+=str(newx-i)+str(newy-j)
                                q.append((newx,newy))
                        #print((i,j),(x,y),path)
                    if path not in check:
                            
                            check.add(path)
                            ans+=1
        #print(check)
        return ans    
    
    def isvalid(self,grid,x,y):
        return x<len(grid) and x>=0 and y>=0 and y<len(grid[0]) and grid[x][y]==1