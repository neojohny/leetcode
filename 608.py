class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if len(nums)<2:
            return None
        left,right = 0,1
        while nums[left]+nums[right]<target:
            right += 1
            if right == len(nums) or nums[left]+nums[right]>target:
                
                left += 1
                right = left + 1
            # if nums[left]+nums[right]==target:
            #     return left+1,right+1
        if nums[left] + nums[right] == target: 
            return left+1,right+1
        else:
            return None
	

	#better solution is going from both end to the middle
    def twoSum_better(self, nums, target):
        # write your code here
        if not nums:# or len(nums)<2:
            return []
        left = 0
        right = len(nums)-1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [left+1,right+1]
            if total > target:
                right -= 1
            
            if total < target:
                left += 1
        return []