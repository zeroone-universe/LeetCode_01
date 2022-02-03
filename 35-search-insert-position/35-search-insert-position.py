class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        if target<=nums[0]:
            return 0
        elif target >nums[-1]:
            return len(nums)
        
        while left<right:
            if right-left==1 or right==left:
                return right
            
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid