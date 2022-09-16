class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        for i in range(len(nums)-2):
            
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            
            idx_left = i+1
            idx_right = len(nums)-1
            
            while idx_left<idx_right:
                summation = nums[i] + nums[idx_left] + nums[idx_right]
                
                if summation > 0 :
                    idx_right -= 1
                elif summation < 0:
                    idx_left += 1
                elif summation == 0:
                    if [nums[i], nums[idx_left], nums[idx_right]] not in result:
                        result.append([nums[i], nums[idx_left], nums[idx_right]])
                        
                    while idx_left < idx_right and nums[idx_right] == nums[idx_right-1]:
                        idx_right -= 1
                    while idx_left < idx_right and nums[idx_left] == nums[idx_left+1]:
                        idx_left += 1
                    
                    
                    idx_right -= 1
                    idx_left += 1
        return result
        