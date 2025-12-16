class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                tree[mgr].append(employee)
        
        max_time = 0

        def dfs(employee):
            if not tree[employee]:
                return 0
            
            max_time = 0
            for zir in tree[employee]:
                max_time = max(max_time, dfs(zir))
            
            return max_time + informTime[employee]
        return dfs(headID)