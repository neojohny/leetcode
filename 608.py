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