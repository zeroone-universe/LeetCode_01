class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dni = []
        for idx in range(len(gas)):
            dni.append(gas[idx]-cost[idx])
            
        if sum(dni)<0 :
            return -1
        
        start, fuel = 0, 0
        
        for idx in range(len(gas)):
            if fuel + dni[idx] < 0:
                start = idx + 1
                fuel = 0
            else:
                fuel += dni[idx]
                
        return start