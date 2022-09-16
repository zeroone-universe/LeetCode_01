class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        
            
        for i in range((len(nums)-1)//2+1):
            summ += nums[2*i]
            
        return summ