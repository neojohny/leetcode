class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return 0
        left = 0
        right = len(A) - 1
        while left +1 < right:

            mid = int(left/2 - right/2 + right)
            #print(left,mid,right)
            if A[mid] > A[mid - 1] and A[mid] > A[mid+1]:
                #print('end')

                return mid
            if A[mid] > A[mid+1]:
                right = mid
            # elif A[mid] > A[mid-1]:
            #     left = mid
            else:
                left = mid
        #print('end')
        if A[left] > A[right]:
            return left
        else:
            return right

