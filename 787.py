from collections import deque
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        s = deque([start])
        visited = [start]
        while s:
            for _ in range(len(s)):
                x,y = s.popleft()
                print([x,y])
                new_pos = self.move(maze,[x,y])
                #print(new_pos)
                for p in new_pos:
                    x,y = p
                    if [x,y] == destination:
                        return True
                    elif [x,y] not in visited:
                        visited.append([x,y])
                        s.append([x,y])
                        #print(s)
        return False
    
    def move(self,maze,pos):
        result = []
        x,y = pos
        while x < len(maze)-1 and maze[x][y] == 0:
            x += 1
        if maze[x][y]==1:
            x -= 1
        result.append([x,y])

        x,y = pos
        while y< len(maze[0])-1 and maze[x][y] == 0:
            y += 1
        if maze[x][y]==1:
            y -= 1
        result.append([x,y])

        x,y = pos
        while  x > 0 and maze[x][y] == 0 :
            x -= 1
        if maze[x][y]==1:
            x+=1
        result.append([x,y])

        x,y = pos
        while y > 0 and maze[x][y] == 0 :
            y -= 1
        if maze[x][y]==1:
            y+=1
        result.append([x,y])
        return result