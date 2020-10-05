class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        
        # length = len(nums)
        # pre = 0
        
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[pre]:
        #         length -= 1
        #         nums = nums[:pre] + nums[pre+1:]
        #         i-=1
        #         #continue
            
        #     else:
        #         pre = i
        
        # return length
        pre = nums[-1]
        
        for i in range(len(nums)-1,1,-1):
            loc = i
            if nums[loc] == nums[loc-1] == nums[loc-2]:
                nums.pop(i)
        
        return len(nums)