class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def dfs(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for w in nums:
                if w not in perm:
                    dfs(perm+[w])
                    
        for i in nums:
            dfs([i])
        
        return result
                    
            