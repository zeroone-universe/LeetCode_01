class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(hap, discovered=[]):
            if hap > target:
                return
            elif hap == target: 
                result.append(discovered[:])
                return
            
            for idx in range(candidates.index(discovered[-1]), len(candidates)):
                dfs(hap+candidates[idx], discovered + [candidates[idx]])
        
        for cand in candidates:
            dfs(cand, [cand])
        
        return result