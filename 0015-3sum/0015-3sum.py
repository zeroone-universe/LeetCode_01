class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            left = i+1
            right = len(nums)-1
            
            while left < right:
                if nums[left]+ nums[right] == -nums[i]:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]]) 
                    left+=1
                    right-=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1

                elif nums[left]+ nums[right] < -nums[i]:
                    left+=1
                
                        
                elif nums[left]+ nums[right] > -nums[i]:
                    right-=1
                 
        return result
            
               