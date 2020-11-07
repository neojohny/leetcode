class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        start = 0
        end = len(A) - 1
        temp = [0]*len(A)
        
        mid = int((start + end) / 2)
        
        self.merge(A,start,end,temp)
        return A
    
    def merge(self,A,start,end,temp):
        if start >= end:
            return
        left = start
        right = end
        mid = int((start+end)/2)
        
        self.merge(A,start,mid,temp)
        self.merge(A,mid+1,end,temp)
        self.mergesort(A,start,end,mid,temp)
    
    def mergesort(self,A,start,end,mid,temp):
        index = start
        left = start
        right = mid+1
        while left < mid+1 and right < end+1:
            if A[left] > A[right]:
                temp[index] = A[right]
                index += 1
                right += 1
            else:
                temp[index] = A[left]
                index += 1
                left += 1
            
        while left < mid+1:
            temp[index] = A[left]
            index += 1
            left += 1
            
        while right < end+1:
            temp[index] = A[right]
            index += 1
            right += 1
            
        A[start:end+1] = temp[start:end+1]