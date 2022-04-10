class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        tot = [i+1 for i in range(0, n)]
        
        def dfs(comb, max_num):
            if len(comb) == k :
                result.append(comb)
                return
            
            for j in tot:
                if j >max_num:
                    new_comb = comb+[j]
                    dfs(new_comb, max(new_comb))
                    
        dfs([],0)
        return result
            
            