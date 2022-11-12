class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def dfs(discovered):
            if len(discovered) == k:
                output.append(list(discovered))
                return 0
            
            if not discovered:
                start = 1
            else:
                start = discovered[-1]+1
                
            for num in range(start, n+1):
                if num not in discovered:
                    dfs(discovered+ [num])
        
        dfs([])
        return output
        