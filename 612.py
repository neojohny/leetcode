"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        # points.sort(key = lambda P: ((P.x-origin.x)**2 + (P.y-origin.y)**2,P.x,P.y))
        # print([[p.x,p.y] for p in points])

        # return points[:k]
        distances = [(self.dis(p,origin),p.x,p.y) for p in points]
        orders = distances.copy()
        print(orders)
        self.order(orders,0,len(orders)-1,k)
        ds = orders[:k]
        #print(orders)
      
        ds = list(set(ds))
        ds.sort()
        result = []
        for d in ds:
          for i in range(len(distances)):
            temp = []
            if d == distances[i]:
              temp.append(points[i])
            if len(temp)>1:
              temp.sort()
            result += temp
        return result[:k]


    def order(self,d,start,end,k):
      left = start
      right = end
      mid = d[(start+end)//2]
      while left <= right:
        while left<=right and d[left] < mid:
          left += 1
        while left <= right and d[right] > mid:
          right-=1
        if left <= right:
          d[left],d[right] = d[right],d[left]
          left += 1
          right -=1

      if k<=right:
        self.order(d,start,right,k)
      if k >= left:
        self.order(d,left,end,k)


    def dis(self,p,o):
      #for x,y in point:
        distance = (p.x-o.x)**2 + (p.y-o.y)**2
        return distance