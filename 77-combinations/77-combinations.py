class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        
        def dfs(perm):
            if len(perm) == k:
                result.append(perm[:])
                return
            
            for w in range(perm[-1],n+1):
                if w not in perm:
                    dfs(perm+[w])
                    
        for i in range(1,n+1):
            dfs([i])
        
        return result