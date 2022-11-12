class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def dfs(discovered):
            if len(discovered) == len(nums):
                output.append(discovered)
            
            for ele in nums:
                if ele not in discovered:
                    new_dis = discovered[:]
                    new_dis.append(ele)
                    dfs(new_dis)
                    
        dfs([])
        
        return output
                    