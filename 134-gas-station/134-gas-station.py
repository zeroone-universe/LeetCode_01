class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) - sum(cost) <0 :
            return -1
        
        start, fuel = 0, 0
        
        for idx in range(len(gas)):
            if fuel + gas[idx]-cost[idx] < 0:
                start = idx + 1
                fuel = 0
            else:
                fuel += (gas[idx]-cost[idx])
                
        return start