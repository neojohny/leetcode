from collections import deque
class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        nodeindegree = [0 for _ in range(numCourses)]
        nodeneighbour = [[] for _ in range(numCourses)]

        for c,pre in prerequisites:
            nodeindegree[pre] += 1
            nodeneighbour[c].append(pre)

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
        
        return len(result) == numCourses
