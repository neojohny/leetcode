https://github.com/neojohny/leetcode.gitclass Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        self.quicksort(A,0,len(A)-1)
        return [self.findnumber(A,i) for i in queries]

    
    def findnumber(self,A,number):
        if len(A) == 0:
            return 0
        if number < A[0]:
            return 0
        if number > A[-1]:
            return len(A)
        start = 0
        end = len(A)-1

        while start+1<end:
            mid = (start + end)//2
            if number>A[mid]:
                start = mid
            else: 
                end = mid
        if A[start] >= number:
            return start
        if A[end] >= number:
            return end
        return end + 1
        
        # left, right = 0, len(nums)-1
        # while left + 1 < right :
        #     mid = (left + right) / 2
        #     if nums[mid] < target :
        #     	left = mid
        #     else :
        #     	right = mid
        # if nums[left] == target :
        #     return left
        # elif nums[right] == target :
        #     return right
        # return -1;
    
    
    def quicksort(self,A,start,end):
        if start>end:
            return
        left = start
        right = end
        mid = A[(start+end)//2]
        while left <= right:
            while left <= right and A[left]<mid:
                left += 1
            
            while left<= right and A[right]>mid:
                right -= 1
            if left <= right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
        self.quicksort(A,start,right)
        self.quicksort(A,left,end)
        
        


