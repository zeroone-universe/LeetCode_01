class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        combs = []
        
        def dfs(comb, start):
            if len(comb) == k:
                combs.append(comb)
                return        
            
            if start > n:
                return
            
            for idx in range(start, n+1, 1):
                dfs(comb+[idx], idx+1)
        
        for v in range(1, n+1, 1):
            dfs([v], v+1)
            
        return combs
        
        