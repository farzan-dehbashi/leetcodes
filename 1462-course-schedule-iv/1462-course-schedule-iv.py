class Solution:
    def checkIfPrerequisite(self, numCourses: int, p: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree, graph, reqs, q = collections.defaultdict(int), collections.defaultdict(list), collections.defaultdict(set), collections.deque()

        for pre, c in p:
            indegree[c] += 1
            graph[pre].append(c)
            reqs[c].add(pre)
        
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        while q:
            cur = q.popleft()
            for c in graph[cur]:
                indegree[c] -= 1
                for req in reqs[cur]:
                    reqs[c].add(req)
                if indegree[c] == 0:
                    q.append(c)
        res = []
        for u, v in queries:
            res.append(u in reqs[v])
        return res

