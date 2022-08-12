class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        
        def check(size):
            for i in range(idx+1, idx+size+1):
                if (i >= len(data)) or data[i] >> 6 !=0b10:
                    return False
            return True
            
        
        
        
        while idx < len(data):
            datum = data[idx]
            if datum >> 3 == 0b11110 and check(3):
                idx+=4
            elif datum >> 4 == 0b1110 and check(2):
                idx+=3
            elif datum >> 5 == 0b110 and check(1):
                idx+=2
            elif datum >> 7 == 0b0:
                idx+=1
            
            else:
                return False
            
        return True
        
        