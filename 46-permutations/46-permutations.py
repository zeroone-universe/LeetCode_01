class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            
            for j in nums:
                if j not in perm: 
                    dfs(perm + [j])
        
        
        dfs([])
        
        return result
                    