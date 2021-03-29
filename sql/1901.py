class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        # write your code here
        # result = [a**2 for a in A]
        # self.sorting(result,0,len(result)-1)
        # #print(result)
        # #result.sort()
        # return result
        lowest = min([abs(i) for i in A])
        if lowest in A:
            left = A.index(lowest)
        else:
            left = A.index(-lowest)

        if left == len(A)-1:
            return [i**2 for i in A]
        right = left + 1
        result = []
        while left >=0 and right<=len(A)-1:
            if abs(A[left]) <= abs(A[right]):
                result.append(A[left]**2)
                left -= 1
            else:
                result.append(A[right]**2)
                right +=1
        #print(left,right)
        if left == -1:
            result += [i**2 for i in A[right:]]
        
        else:
            result += [i**2 for i in A[:left+1]]
        
        return result


    def sorting(self,A,start,end):
        if start >= end:
            return

        left = start
        right = end
        mid = A[(left+right)//2]
        while left <= right:
            while A[left] < mid and left <=right:
                left += 1
            
            while A[right] > mid and left <=right:
                right -=1
            if left<=right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
        
        self.sorting(A,start,right)
        self.sorting(A,left,end)
