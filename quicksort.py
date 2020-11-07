class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        start = 0
        end = len(A) - 1

        
        self.quicksort(A,start,end)
        
        return A
    
    def quicksort(self,A,start,end):
        if start>=end:
            return
        mid = A[(start+end)//2]    
        left = start
        right = end
        
        while left<=right:
            while A[left] < mid and left <= right:
                left += 1
            
            while  A[right]>mid and left<=right:
                right-=1
            
            if left<=right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
            
        self.quicksort(A,start,right)
        self.quicksort(A,left,end)
            