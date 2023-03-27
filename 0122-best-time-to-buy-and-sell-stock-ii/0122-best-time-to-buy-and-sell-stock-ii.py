class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        keep = sys.maxsize
        profit = 0
        for idx in range(len(prices)):
            if idx == 0:
                keep =  prices[idx]
                continue
            
            if prices[idx] > keep:
                profit += prices[idx] - keep
                keep = prices[idx]
            else:
                keep = prices[idx]
            
            
        return profit