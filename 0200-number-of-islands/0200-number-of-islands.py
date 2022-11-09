class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i != 0:
                    dfs(i-1,j)
                
                try:
                    dfs(i+1,j)
                except:
                    pass
                    
                if j != 0:
                    dfs(i,j-1)
                
                try:
                    dfs(i,j+1)
                except:
                    pass
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    result += 1

                    
        return result