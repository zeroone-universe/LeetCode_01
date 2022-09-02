class Solution:
    def fib(self, n: int) -> int:        
        dp = list()
        dp.append(0)
        dp.append(1)
        
        if n<2:
            return dp[n]
        
        for idx in range(2, n):
            dp.append(dp[idx-1]+dp[idx-2])
            
        return dp[n-1] + dp[n-2]
            