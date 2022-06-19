class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:
            return [0]
        
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        leaves = []
        for idx in range(n+1):
            if len(graph[idx]) == 1:
                leaves.append(idx)
                
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neigh = graph[leaf].pop()
                graph[neigh].remove(leaf)
                
                if len(graph[neigh]) == 1:
                    new_leaves.append(neigh)
            
            leaves = new_leaves
            
        return leaves