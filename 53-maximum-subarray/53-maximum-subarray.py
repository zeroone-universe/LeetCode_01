class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for idx in range(1,len(nums)):
            nums[idx] += nums[idx-1] if nums[idx-1]>=0 else 0
            
        return max(nums)