class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums)//2-1
        if nums[mid] < nums[-1]:
            return self.findMin(nums[:mid+1])
        
        if nums[mid] > nums[-1]:
            return self.findMin(nums[mid+1:])
        
        if nums[mid] == nums[-1]:
            if nums[0] < nums[mid]:
                return nums[0]
            
            if nums[0] > nums[mid]:
                return nums[mid]
            
            if sum(nums[:mid+1])/len(nums[:mid+1]) == nums[0]:
                return self.findMin(nums[mid+1:])
            else:
                #print('here')
                return self.findMin(nums[:mid+1])