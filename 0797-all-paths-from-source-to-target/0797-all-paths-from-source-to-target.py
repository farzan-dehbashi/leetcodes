class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, adjs = [], defaultdict(set)
        for start in range(len(graph)):
            for end in graph[start]:
                adjs[start].add(end)
        
        def dfs(start, end, cur):
            if start == end:
                res.append(cur[:])
                return
            
            for nei in adjs[start]:
                cur.append(nei)
                dfs(nei, end, cur)
                cur.pop()
        
        dfs(0, len(graph) - 1, [0])
        return res