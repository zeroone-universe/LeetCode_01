class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        def dfs(subset, index):
            result.append(subset[:])
            if index == len(nums)-1:
                return
            
            for i in range(index+1, len(nums)):
                dfs(subset + [nums[i]], i)
            
        dfs([], -1)
        return result
            
            
        
        