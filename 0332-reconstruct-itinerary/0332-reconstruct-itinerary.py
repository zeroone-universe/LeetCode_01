class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)
            
        dfs("JFK")
        route.reverse()
        return route
            