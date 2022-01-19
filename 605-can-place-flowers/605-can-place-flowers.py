class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num=0
        
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                num=1
            return num>=n
        
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                continue
                
            if i>0 and i<len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    num+=1
            elif i==0:
                if flowerbed[i+1]==0:
                    flowerbed[i]=1
                    num+=1
            elif i==len(flowerbed)-1:
                if flowerbed[i-1]==0:
                    flowerbed[i]=1
                    num+=1
                    
        return num>=n