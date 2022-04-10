class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_cand = sorted(candidates)
        
        def dfs(nums, index):
            if sum(nums) == target:
                result.append(nums[:])
                return
            elif sum(nums) > target:
                return
            
            for i in range(index, len(sorted_cand)):
                dfs(nums+[sorted_cand[i]],i)
                
        dfs([], 0)
        return result