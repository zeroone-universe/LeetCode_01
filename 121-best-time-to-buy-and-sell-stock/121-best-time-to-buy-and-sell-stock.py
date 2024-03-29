class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        lowest=sys.maxsize
        
        for i in range(len(prices)):
            max_price=max(max_price, prices[i]-lowest)
            lowest=min(lowest, prices[i])
            
        
        return max_price
        