from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if not numCourses:
            return []
        nodeindegree = [0 for _ in range(numCourses)]
        nodeneighbour = [[] for _ in range(numCourses)]

        for c,pre in prerequisites:
            nodeindegree[c] += 1
            nodeneighbour[pre].append(c)

        startcourse = []
        for i in range(numCourses):
            if not nodeindegree[i]:
                startcourse.append(i)
        q = deque(startcourse)
        result = []
        while q:
            head = q.popleft()
            result.append(head)
            nei = nodeneighbour[head]
            for n in nei:
                nodeindegree[n] -= 1
                if nodeindegree[n] == 0:
                    q.append(n)
        
        if len(result) == numCourses:
            return result[::-1]
        
        else:
            return []
