class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        tot = [i+1 for i in range(0, n)]
        
        
        return list(itertools.combinations(tot, k ))