class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start/2 - end/2 + end)
            if nums[mid] > target:
                end = mid
            if nums[mid] <= target:
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1