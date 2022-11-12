class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        
        def dfs(idx_last, comb):
            if sum(comb) == target:
                output.append(comb)
                
            elif sum(comb) < target:
                for idx in range(idx_last, len(candidates)):
                    if candidates[idx] <= target:
                        dfs(idx, comb+[candidates[idx]])
                        
        dfs(0, [])
        
        return output