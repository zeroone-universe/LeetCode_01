class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)
        
        mult = 1
        for i in range(1, len(nums)):
            mult *=nums[i-1]
            output[i] = output[i]*mult
            
        mult = 1
        for i in range(len(nums)-2, -1, -1):
            mult *= nums[i+1]
            output[i] = output[i]*mult
            
        return output