class Solution(object):
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binarysearch(idx_l, idx_r):
            if idx_l <= idx_r:
                idx_c = (idx_l+idx_r)//2
                
                if nums[idx_c] == target:
                    return idx_c
                elif nums[idx_c] < target:
                    return binarysearch(idx_c+ 1, idx_r)
                elif nums[idx_c] > target:
                    return binarysearch(idx_l, idx_c-1)
            
            
            
            else:
                return -1
            
        return binarysearch(0, len(nums)-1)
        