class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num=collections.defaultdict(int)
        for char in stones:
            num[char]+=1
            
        total=0
        for i in jewels:
            total+=num[i]
        
        return total
                
            