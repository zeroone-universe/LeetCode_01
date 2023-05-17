class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = 0
        for idx in range(1, len(nums),1):
            if nums[idx-1] > nums[idx]:
                pivot = idx
                
        
        
        
        
        def bs(idx_left, idx_right):
            if idx_left <= idx_right:
                
                idx_mid = (idx_left+idx_right)//2
                idx_mid_rot = (idx_mid+pivot) % len(nums)
                
                if nums[idx_mid_rot] == target:
                    return idx_mid_rot
                elif nums[idx_mid_rot] < target:
                    return bs(idx_mid+1, idx_right)
                elif nums[idx_mid_rot] > target:
                    return bs(idx_left, idx_mid-1)
                    
            else:
                return -1
            
        return bs(0, len(nums))
            