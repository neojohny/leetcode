class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # new_color = [0]*k
        # for c in colors:
        #   new_color[c-1] += 1
        # result = sum([[i+1] * new_color[i] for i in range(k)],[])
        # colors = result.copy()

        self.helper(colors,0,len(colors)-1,1,k)

    def helper(self,colors,start,end,cs,ce):
      if start >= end or cs >= ce:
        return
      #mid = colors[(start + end)//2]
      mid = (cs + ce)//2
      left = start
      right = end
      while left <= right:
        while left <=right and colors[left] <= mid:
          left += 1

        while left <=right and colors[right] > mid:
          right -= 1
        
        if left <= right:
          colors[left],colors[right] = colors[right],colors[left]
          left += 1
          right -= 1

      self.helper(colors,start,right,cs,mid)
      self.helper(colors,left,end,mid+1,ce)