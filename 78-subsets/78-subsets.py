class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(subset):
            result.append(subset[:])
            if subset[-1] == nums[-1]:
                return
            for idx in range(nums.index(subset[-1])+1, len(nums)):
                dfs(subset + [nums[idx]])
        
        for num in nums:
            dfs([num])
            
        result.append([])
        return result
        