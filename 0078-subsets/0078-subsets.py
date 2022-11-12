class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        
        def dfs(idx_last, subset):
            output.append(subset)
            
            for idx in range(idx_last+1, len(nums)):
                dfs(idx, subset+[nums[idx]])
                
        dfs(-1, [])
        return output