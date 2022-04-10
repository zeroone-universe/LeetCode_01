class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(nums, index):
            if sum(nums) == target:
                result.append(nums[:])
                return
            elif sum(nums) > target:
                return
            
            for i in range(index, len(candidates)):
                dfs(nums+[candidates[i]],i)
                
        dfs([], 0)
        return result