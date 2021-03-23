class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return []
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int(left/2 - right/2 + right)
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid

        if nums[left] >= nums[right]:
            return nums[left]
        if nums[right] >= nums[left]:
            return nums[right]
        
