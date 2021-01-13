class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        
        pieces = 0
        left = 1
        right = max(L)
        
        while left + 1 < right:
            mid = (left + right)//2
            pieces = self.getpiece(L,mid)
            # if pieces == k:
            #     return mid
            
            if pieces < k:
                right = mid
            else:
                left = mid
        if self.getpiece(L,right) >= k:
            return right
        if self.getpiece(L,left) >= k:
            return left
        
        return 0 
            
            
        
    
    def getpiece(self,L,length):
        pieces = 0
        for l in L:
            pieces += l//length
        
        return pieces