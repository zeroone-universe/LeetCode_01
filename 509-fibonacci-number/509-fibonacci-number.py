class Solution:
    
    
    def fib(self, n: int) -> int:        
        dp = collections.defaultdict(int)
        
        dp[0] = 0
        dp[1] = 1
        
        if n<2:
            return dp[n]
        
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
            
        return dp[n]