class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        output = 0
        freq = collections.defaultdict(int)
        
        for stone in stones:
            freq[stone] += 1
            
        for jewel in jewels:
            output+=freq[jewel]
            
        return output