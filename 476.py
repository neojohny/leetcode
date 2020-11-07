class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        return self.combine(0,len(A)-1,A,{})
    
    
    def combine(self,start,end,A,memo):
        if start >= end:
            return 0
            
        minimum = float('inf')
        cost = sum(A[start:end+1])
        if (start,end) in memo:
            return memo[(start,end)]
        
        for mid in range(start,end):
            left = self.combine(start,mid,A,memo)
            right = self.combine(mid+1,end,A,memo)
            minimum = min(minimum,left+right+cost)
            
        memo[(start,end)] = minimum
        return minimum