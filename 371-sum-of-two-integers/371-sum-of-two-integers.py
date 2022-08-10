class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        POS_MAX = 0x7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        SUM = 0
        CARRY = 0
        
        result = []
        for i in range(32):
            A = int(a_bin[31-i])
            B = int(b_bin[31-i])
            
            Q1 = A & B
            Q2 = A ^ B
            SUM = Q2 ^ CARRY
            Q3 = CARRY & Q2
            CARRY = Q1 | Q3
            
            result.append(str(SUM))
            
        if CARRY == 1:
            result.append("1")
            
        result = int("".join(result[::-1]), 2) & MASK
        
        if result > POS_MAX:
            result = ~(result^MASK)
            
        return result